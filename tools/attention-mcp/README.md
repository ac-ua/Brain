# Apps attention — the cockpit's connector to the apps

A remote MCP server on Cloudflare Workers. It gives « Brain · Cockpit » (a claude.ai artifact, which cannot `fetch`
other hosts) what waits on Aurélien in each app: one tool, `get_attention`, which reads `GET /api/attention` of every
app listed in `skills/web-design-system/apps.json` and merges the answers (`docs/platform.md` › The attention contract).
Why this option and not a Notion job: `docs/platform.md` › Thread 4 decisions.

| | |
|---|---|
| Address | `https://attention-mcp.a-caye.workers.dev/mcp` (Streamable HTTP, JSON responses, stateless) |
| Tool | `get_attention({ app? })` → `{ generated_at, total, apps: [{ app, name, url, ok, error?, generated_at, items[] }] }`; read-only |
| Who may connect | OAuth 2.1 (`@cloudflare/workers-oauth-provider`): claude.ai registers itself, Aurélien allows that client on `/authorize`, then signs in with Cloudflare Access (an OIDC « SaaS » application of the team, Google login); only an e-mail of `ALLOWED_EMAILS` gets a token (scope `attention:read`, 1 h, refreshed) |
| How it reads the apps | one Access service token, `hub-attention`, admitted by « Apps · Aurélien » (`ac-ua/sport` › `docs/access.md` › Machine callers); the apps' Functions verify the JWT Access forwards |
| Storage | KV `OAUTH_KV`: clients and grants, hashed by the library; no app data |
| Cost | Workers free plan (100 k requests a day); no cron; one KV namespace |
| Release | Workers Builds connected to `ac-ua/brain`, root `tools/attention-mcp`: a merge into `main` that touches it deploys it. Never `wrangler deploy` from a session |
| Checks | `npm test` (fan-out and MCP layer, fake fetch), `npm run check` (bundle dry run) |

The cockpit declares it in its `mcp` capability as server **`Apps attention`** (exact display name), tool
`get_attention`; it shows the items under « Dans tes apps » and the counts in its Apps group and app switcher.

## Setup (Aurélien, once; ~15 minutes)
Order matters: the Worker needs its KV id before its first build, and the connector needs the Worker's secrets.

1. **KV namespace.** dash.cloudflare.com › Storage & databases › Workers KV › *Create instance* · name
   `attention-mcp-oauth` › Create. Copy its **ID** (not a secret) and paste it to Claude in a session (or edit
   `tools/attention-mcp/wrangler.toml` on GitHub: `id = "…"` under `[[kv_namespaces]]`, commit to `main`).
2. **OIDC application for the sign-in.** one.dash.cloudflare.com › team `wild-snow-bb5e` › Access controls ›
   Applications › *Add an application* › **SaaS** › Application: `Apps · attention (connecteur)` (type it, then
   *Add as custom application*) › Authentication protocol **OIDC** › Redirect URLs:
   `https://attention-mcp.a-caye.workers.dev/callback` › Scopes: `openid`, `email` › leave *PKCE without client
   secret* off › Next › Policies: *Add a policy* « Aurélien » · Action Allow · Include · Emails = your Google address
   (the same as « Apps · Aurélien ») › Login methods: Google only › Save. Copy **Client ID** and **Client secret**.
3. **Service token for reading the apps.** Same dashboard › Access controls › Service credentials › Service tokens ›
   *Create service token* · name `hub-attention` · duration 1 year › Generate. Copy **Client ID** and **Client
   secret** (shown once). Then Applications › « Apps · Aurélien » › Policies › *Add a policy*: name
   `Service · hub-attention`, Action **Service Auth**, Include › Service Token › `hub-attention` › Save.
4. **The Worker, built from the repo.** dash.cloudflare.com › Workers & Pages › *Create* › Workers › *Import a
   repository* › GitHub › `ac-ua/brain` › Project name `attention-mcp` › *Advanced settings*: Root directory
   `tools/attention-mcp`, Build command `npm ci`, Deploy command `npx wrangler deploy`, Production branch `main`,
   Build watch paths: include `tools/attention-mcp/*` and `skills/web-design-system/apps.json` › Create and deploy.
5. **Its secrets.** Workers & Pages › `attention-mcp` › Settings › Variables and Secrets › *Add* (type **Secret**),
   one by one: `OIDC_CLIENT_ID` and `OIDC_CLIENT_SECRET` (step 2), `ACCESS_CLIENT_ID` and `ACCESS_CLIENT_SECRET`
   (step 3), `ALLOWED_EMAILS` (your Google address) › Deploy.
6. **The connector in claude.ai.** claude.ai › Settings › Connectors › *Add custom connector* · Name
   **`Apps attention`** (exactly) · URL `https://attention-mcp.a-caye.workers.dev/mcp` › Add › Connect: the page
   « Autoriser Claude ? » › Autoriser › Google sign-in through Access › back in claude.ai, connected.
7. **The cockpit.** Open « Brain · Cockpit » › Actualiser › allow « Apps attention » for the page. « Dans tes apps »
   lists the items; an app that refuses the token says so in its own line.

## Security notes
- The service token opens every app of « Apps · Aurélien »; each app limits it (Finance: `GET /api/attention` and
  `/api/health` only, v0.6; Sport: its API is read-only). **Camp de Base still lets a service token write**: its next
  release limits tokens to `GET /api/attention` and `/api/health` (Build Roadmap). Until then the token's secret lives
  only in this Worker's secrets.
- The consent page shows the client's name and where the code goes; never allow a client you did not just add.
- To cut access: claude.ai › Connectors › remove; Access › Service tokens › revoke `hub-attention`; or delete the KV
  entries of the grant.
