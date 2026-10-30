// A minimal, stateless MCP server (Streamable HTTP, JSON responses only): initialize, ping, tools/list, tools/call.
// One read-only tool, get_attention. The OAuth layer (index.js) has already checked the bearer token.
import { APPS, getAttention } from "./attention.js";

const PROTOCOLS = ["2025-06-18", "2025-03-26", "2024-11-05"];
const TOOL = {
  name: "get_attention",
  title: "Ce qui attend Aurélien dans ses apps",
  description: "Lit GET /api/attention de chaque app perso (Camp de Base, Sport, Finance) et renvoie leurs éléments : " +
    "titre en français, sévérité (bad, warn, info), type (alert, deadline, decision, review), échéance et lien vers " +
    "l'endroit de l'app où on le règle. Lecture seule. Une app en échec revient avec ok: false et la raison.",
  inputSchema: {
    type: "object",
    properties: { app: { type: "string", enum: APPS.map((a) => a.key), description: "Une seule app ; toutes si absent." } },
    additionalProperties: false,
  },
  annotations: { readOnlyHint: true, openWorldHint: false },
};

const reply = (id, result) => ({ jsonrpc: "2.0", id, result });
const fail = (id, code, message) => ({ jsonrpc: "2.0", id, error: { code, message } });

async function handle(msg, env, fetchImpl) {
  const { id, method, params } = msg || {};
  if (id === undefined || id === null) return null; // a notification (initialized, cancelled): nothing to answer
  if (method === "initialize") {
    const asked = params && params.protocolVersion;
    return reply(id, {
      protocolVersion: PROTOCOLS.includes(asked) ? asked : PROTOCOLS[0],
      capabilities: { tools: { listChanged: false } },
      serverInfo: { name: "brain-attention", title: "Apps · attention", version: "1.0.0" },
    });
  }
  if (method === "ping") return reply(id, {});
  if (method === "tools/list") return reply(id, { tools: [TOOL] });
  if (method === "tools/call") {
    if (!params || params.name !== TOOL.name) return fail(id, -32602, `Unknown tool: ${params && params.name}`);
    const app = params.arguments && params.arguments.app;
    if (app != null && !APPS.some((a) => a.key === app)) return fail(id, -32602, `Unknown app: ${app}`);
    const data = await getAttention(env, app || null, fetchImpl);
    return reply(id, { content: [{ type: "text", text: JSON.stringify(data) }], structuredContent: data, isError: false });
  }
  return fail(id, -32601, `Method not found: ${method}`);
}

export async function mcpFetch(request, env, fetchImpl = fetch) {
  if (request.method !== "POST") return new Response("Method Not Allowed", { status: 405, headers: { Allow: "POST" } });
  let body;
  try { body = await request.json(); } catch { return Response.json(fail(null, -32700, "Parse error"), { status: 400 }); }
  const batch = Array.isArray(body);
  const out = (await Promise.all((batch ? body : [body]).map((m) => handle(m, env, fetchImpl)))).filter(Boolean);
  if (!out.length) return new Response(null, { status: 202 });
  return Response.json(batch ? out : out[0], { headers: { "Cache-Control": "no-store" } });
}
