// « Apps · attention »: a remote MCP server for claude.ai (custom connector) that reads what waits on Aurélien in his
// apps (docs/platform.md › The attention contract). The Brain cockpit artifact cannot fetch other hosts (CSP); it calls
// this connector through its `mcp` capability instead.
//
// Who may connect: claude.ai registers itself (OAuth 2.1, dynamic registration or a client metadata document); the
// /authorize page asks Aurélien to allow that client, then signs him in with Cloudflare Access (an OIDC « SaaS »
// application of the team, Google login, same policy as the apps), and only an e-mail of ALLOWED_EMAILS gets a token.
// The Worker then reads each app's /api/attention with its own Access service token. Nothing is stored but the OAuth
// grants (KV OAUTH_KV, hashed by the library).
import { OAuthProvider } from "@cloudflare/workers-oauth-provider";
import { mcpFetch } from "./mcp.js";

// The connector's address (workers.dev of the account « a-caye », as sport-sync). Change it here if it ever moves.
const ORIGIN = "https://attention-mcp.a-caye.workers.dev";
const oidc = (env, path) => `https://${env.ACCESS_TEAM_DOMAIN}/cdn-cgi/access/sso/oidc/${env.OIDC_CLIENT_ID}/${path}`;
const esc = (t) => String(t ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const page = (title, body, headers = new Headers(), status = 200) => {
  headers.set("Content-Type", "text/html; charset=utf-8");
  headers.set("Cache-Control", "no-store");
  return new Response(`<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(title)}</title><style>body{font:16px/1.5 system-ui,sans-serif;margin:0;background:#f6f9fd;color:#000}main{max-width:460px;margin:12vh auto;padding:24px;background:#fff;border:1px solid #d6e1ec;border-radius:12px}
h1{font-size:22px;margin:0 0 12px}p{margin:0 0 12px;color:#5b6b7a}b{color:#000}.row{display:flex;gap:8px;margin-top:18px}button{font:inherit;padding:8px 14px;border-radius:8px;border:1px solid #d6e1ec;background:#fff;cursor:pointer}
button.ok{background:#0a6aa7;color:#fff;border-color:#0a6aa7;border-radius:2px}</style><main>${body}</main></html>`, { status, headers });
};
const allowed = (env, email) => {
  const list = String(env.ALLOWED_EMAILS || "").toLowerCase().split(/[\s,]+/).filter(Boolean);
  return !!email && list.includes(String(email).toLowerCase());
};
const b64url = (buf) => btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
const claims = (jwt) => JSON.parse(atob(jwt.split(".")[1].replace(/-/g, "+").replace(/_/g, "/")));

async function authorize(request, env) {
  const url = new URL(request.url), p = env.OAUTH_PROVIDER;
  if (!env.OIDC_CLIENT_ID || !env.OIDC_CLIENT_SECRET || !env.ALLOWED_EMAILS) return page("Connecteur non configuré", "<h1>Connecteur non configuré</h1><p>Il manque OIDC_CLIENT_ID, OIDC_CLIENT_SECRET ou ALLOWED_EMAILS sur le Worker.</p>", undefined, 503);
  if (request.method === "GET" && url.pathname === "/authorize") {
    let req;
    try { req = await p.parseAuthRequest(request); } catch (e) { return e.redirectTo ? Response.redirect(e.redirectTo, 302) : page("Demande invalide", `<h1>Demande invalide</h1><p>${esc(e.description || e.message)}</p>`, undefined, 400); }
    const who = await p.describeConsent(req);
    const { handle, headers } = await p.beginConsent(req);
    return page("Autoriser l'accès", `<h1>Autoriser ${esc(who.clientName || "ce client")} ?</h1>${who.clientDomain ? `<p>Domaine vérifié : <b>${esc(who.clientDomain)}</b></p>` : "<p>Nom déclaré par le client, non vérifié.</p>"}
<p>Il pourra lire <b>ce qui t'attend dans tes apps</b> (Camp de Base, Sport, Finance) : les titres, sévérités et liens de <code>/api/attention</code>. Lecture seule.</p>
<p>Retour vers : <b>${esc(who.redirectHost || new URL(req.redirectUri).host)}</b>. Ensuite, connexion Google par Cloudflare Access.</p>
<form method="post" action="/authorize"><input type="hidden" name="handle" value="${esc(handle)}"><div class="row">
<button class="ok" name="decision" value="allow">Autoriser</button><button name="decision" value="deny">Refuser</button></div></form>`, headers);
  }
  if (request.method === "POST" && url.pathname === "/authorize") {
    const form = await request.formData(), handle = String(form.get("handle") || "");
    try {
      if (form.get("decision") !== "allow") { const d = await p.denyConsent(request, handle); return new Response(null, { status: 302, headers: d.headers }); }
      const ok = await p.approveConsent(request, handle);
      const verifier = b64url(crypto.getRandomValues(new Uint8Array(32)));
      const challenge = b64url(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(verifier)));
      const up = await p.beginUpstream(ok.request, { data: { verifier }, headers: ok.headers });
      const to = new URL(oidc(env, "authorization"));
      to.search = new URLSearchParams({ client_id: env.OIDC_CLIENT_ID, response_type: "code", scope: "openid email",
        redirect_uri: `${url.origin}/callback`, state: up.state, code_challenge: challenge, code_challenge_method: "S256" }).toString();
      up.headers.set("Location", to.toString());
      return new Response(null, { status: 302, headers: up.headers });
    } catch (e) {
      return page("Demande expirée", `<h1>Demande expirée</h1><p>${esc(e.description || "Recommence depuis claude.ai.")}</p>`, undefined, 400);
    }
  }
  return new Response("Not found", { status: 404 });
}

async function callback(request, env) {
  const url = new URL(request.url), p = env.OAUTH_PROVIDER;
  let resumed;
  try { resumed = await p.finishUpstream(request); } catch (e) { return page("Demande expirée", `<h1>Demande expirée</h1><p>${esc(e.description || "Recommence depuis claude.ai.")}</p>`, undefined, 400); }
  const code = url.searchParams.get("code");
  if (!code) return page("Connexion refusée", "<h1>Connexion refusée</h1><p>Cloudflare Access n'a pas renvoyé de code.</p>", undefined, 403);
  const res = await fetch(oidc(env, "token"), {
    method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ grant_type: "authorization_code", code, redirect_uri: `${url.origin}/callback`, client_id: env.OIDC_CLIENT_ID,
      client_secret: env.OIDC_CLIENT_SECRET, code_verifier: resumed.data.verifier }),
  });
  if (!res.ok) return page("Connexion refusée", `<h1>Connexion refusée</h1><p>Échange du code refusé par Access (HTTP ${res.status}).</p>`, undefined, 502);
  // The id_token comes straight from Access's token endpoint over TLS, authenticated with the client secret
  // (OpenID Connect Core 3.1.3.7): its claims are checked, not its signature.
  let c;
  try { c = claims((await res.json()).id_token); } catch { return page("Connexion refusée", "<h1>Connexion refusée</h1><p>Réponse d'Access illisible.</p>", undefined, 502); }
  const now = Date.now() / 1000;
  const aud = Array.isArray(c.aud) ? c.aud : [c.aud];
  if (!aud.includes(env.OIDC_CLIENT_ID) || !(c.exp > now) || !String(c.iss || "").startsWith(`https://${env.ACCESS_TEAM_DOMAIN}`)) return page("Connexion refusée", "<h1>Connexion refusée</h1><p>Jeton d'identité invalide.</p>", undefined, 403);
  if (!allowed(env, c.email)) return page("Accès refusé", `<h1>Accès refusé</h1><p>${esc(c.email)} n'est pas autorisé sur ce connecteur.</p>`, undefined, 403);
  const { redirectTo } = await p.completeAuthorization({ request: resumed.request, userId: encodeURIComponent(c.email), metadata: { label: "Apps · attention" },
    scope: ["attention:read"], props: { email: c.email } });
  resumed.headers.set("Location", redirectTo);
  return new Response(null, { status: 302, headers: resumed.headers });
}

const defaultHandler = {
  async fetch(request, env) {
    const path = new URL(request.url).pathname;
    if (path === "/authorize") return authorize(request, env);
    if (path === "/callback") return callback(request, env);
    if (path === "/") return page("Apps · attention", "<h1>Apps · attention</h1><p>Connecteur MCP du cockpit Brain. Point d'entrée : <code>/mcp</code>.</p>");
    return new Response("Not found", { status: 404 });
  },
};

export default new OAuthProvider({
  apiRoute: "/mcp",
  apiHandler: { fetch: (request, env) => mcpFetch(request, env) },
  defaultHandler,
  authorizeEndpoint: "/authorize",
  tokenEndpoint: "/token",
  clientRegistrationEndpoint: "/register",
  clientIdMetadataDocumentEnabled: true,
  scopesSupported: ["attention:read"],
  requiredScopes: ["attention:read"],
  resourceMetadata: { resource: `${ORIGIN}/mcp`, authorization_servers: [ORIGIN] },
  accessTokenTTL: 3600,
});
