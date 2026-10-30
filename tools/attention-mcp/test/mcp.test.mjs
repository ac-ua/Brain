// npm test  (the MCP layer and the fan-out, with a fake fetch; the OAuth layer is the library's)
import { test } from "node:test";
import assert from "node:assert/strict";
import { getAttention, readApp, APPS } from "../src/attention.js";
import { mcpFetch } from "../src/mcp.js";

const env = { ACCESS_CLIENT_ID: "id", ACCESS_CLIENT_SECRET: "secret" };
const okBody = (app) => ({ app, generated_at: "2026-10-30T07:00:00Z", items: [{ id: "x:1", title: "Un truc à faire", severity: "warn", kind: "review", due: null, url: "https://sport.aureliencaye.com/#data" }] });

test("every app with an attention address is read with the service token", async () => {
  const seen = [];
  const fake = async (url, init) => { seen.push([url, init.headers["CF-Access-Client-Id"], init.redirect]); return new Response(JSON.stringify(okBody("a"))); };
  const r = await getAttention(env, null, fake);
  assert.equal(r.apps.length, APPS.length);
  assert.equal(APPS.length, 3);
  assert.ok(seen.every(([, id, redirect]) => id === "id" && redirect === "manual"));
  assert.equal(r.total, 3);
});

test("one app failing keeps the others", async () => {
  const fake = async (url) => url.includes("finance") ? new Response("", { status: 302 }) : new Response(JSON.stringify(okBody("a")));
  const r = await getAttention(env, null, fake);
  const fin = r.apps.find((a) => a.app === "finance");
  assert.equal(fin.ok, false);
  assert.match(fin.error, /Access/);
  assert.equal(r.apps.filter((a) => a.ok).length, 2);
});

test("no service token: a clear error, no call", async () => {
  let called = false;
  const r = await readApp(APPS[0], {}, async () => { called = true; });
  assert.equal(r.ok, false); assert.equal(called, false);
});

test("items are cleaned: unknown severity → info, non-https url → the app", async () => {
  const fake = async () => new Response(JSON.stringify({ items: [{ id: 1, title: "t", severity: "boom", url: "javascript:alert(1)" }] }));
  const r = await readApp(APPS[0], env, fake);
  assert.equal(r.items[0].severity, "info");
  assert.equal(r.items[0].url, APPS[0].url);
});

test("MCP: initialize, tools/list, tools/call, notification", async () => {
  const call = async (body) => mcpFetch(new Request("https://x/mcp", { method: "POST", body: JSON.stringify(body) }), env, async () => new Response(JSON.stringify(okBody("a"))));
  const init = await (await call({ jsonrpc: "2.0", id: 1, method: "initialize", params: { protocolVersion: "2025-06-18" } })).json();
  assert.equal(init.result.protocolVersion, "2025-06-18");
  const list = await (await call({ jsonrpc: "2.0", id: 2, method: "tools/list" })).json();
  assert.equal(list.result.tools[0].name, "get_attention");
  const res = await (await call({ jsonrpc: "2.0", id: 3, method: "tools/call", params: { name: "get_attention", arguments: { app: "sport" } } })).json();
  assert.equal(res.result.structuredContent.apps.length, 1);
  assert.equal((await call({ jsonrpc: "2.0", method: "notifications/initialized" })).status, 202);
});
