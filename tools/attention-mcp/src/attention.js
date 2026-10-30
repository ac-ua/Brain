// The attention fan-out: read GET /api/attention of every app in the registry (skills/web-design-system/apps.json),
// with this Worker's Cloudflare Access service token, and merge the answers. Read-only. One app failing never hides
// the others: it comes back with ok: false and a French reason.
import registry from "../../../skills/web-design-system/apps.json" with { type: "json" };

const TIMEOUT_MS = 8000;
const RANK = { bad: 0, warn: 1, info: 2 };

export const APPS = registry.apps.filter((a) => a.attention);

const reason = (status) =>
  status === 401 || status === 403 ? "accès refusé : le jeton de service n'est pas admis par l'application Access"
  : status === 302 ? "redirigé vers la connexion Access : le jeton de service manque ou n'est pas admis"
  : status === 404 ? "pas de /api/attention à cette adresse"
  : `réponse HTTP ${status}`;

export async function readApp(app, env, fetchImpl = fetch) {
  const base = { app: app.key, name: app.name, url: app.url };
  if (!env.ACCESS_CLIENT_ID || !env.ACCESS_CLIENT_SECRET) return { ...base, ok: false, error: "jeton de service Access non configuré sur le connecteur" };
  const ctl = new AbortController();
  const timer = setTimeout(() => ctl.abort(), TIMEOUT_MS);
  try {
    const res = await fetchImpl(app.attention, {
      headers: { "CF-Access-Client-Id": env.ACCESS_CLIENT_ID, "CF-Access-Client-Secret": env.ACCESS_CLIENT_SECRET, Accept: "application/json" },
      redirect: "manual", signal: ctl.signal,
    });
    if (!res.ok) return { ...base, ok: false, error: reason(res.status) };
    const body = await res.json();
    const items = (Array.isArray(body.items) ? body.items : []).slice(0, 20).map((i) => ({
      id: String(i.id ?? ""), title: String(i.title ?? ""), severity: RANK[i.severity] != null ? i.severity : "info",
      kind: i.kind || "review", due: i.due ?? null, url: typeof i.url === "string" && i.url.startsWith("https://") ? i.url : app.url,
    }));
    return { ...base, ok: true, generated_at: body.generated_at || null, items };
  } catch (e) {
    return { ...base, ok: false, error: e && e.name === "AbortError" ? "pas de réponse en 8 s" : "injoignable" };
  } finally {
    clearTimeout(timer);
  }
}

export async function getAttention(env, only, fetchImpl = fetch) {
  const apps = only ? APPS.filter((a) => a.key === only) : APPS;
  const results = await Promise.all(apps.map((a) => readApp(a, env, fetchImpl)));
  const total = results.reduce((n, r) => n + (r.items ? r.items.length : 0), 0);
  return { generated_at: new Date().toISOString().slice(0, 19) + "Z", total, apps: results };
}
