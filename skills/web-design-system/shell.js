// Design-system app shell (Camp de Base's side menu, made generic): fold the side menu to icons (kept per app), open it
// as a drawer on phones, and the theme switch (Auto · Light · Dark). Copy it next to the app's pages and load it after
// the markup (SKILL.md › Shell). It only toggles classes and attributes; every text lives in the HTML.
// Markup: a root with data-ds-shell (else <body>) and data-ds-app="<app>" (storage keys <app>.side.mini, <app>.theme),
// .ds-side-fold[data-ds-side-fold] in .ds-side-brand, [data-ds-side-open] in .ds-mtop, .ds-scrim[data-ds-scrim],
// theme buttons [data-ds-theme="auto|light|dark"] in .ds-side-foot.
(() => {
  const start = () => {
    const root = document.querySelector("[data-ds-shell]") || document.body;
    const app = root.dataset.dsApp || document.body.dataset.dsApp || "app";
    const html = document.documentElement;
    const get = (k) => { try { return localStorage.getItem(`${app}.${k}`); } catch { return null; } };
    const set = (k, v) => { try { localStorage.setItem(`${app}.${k}`, v); } catch { /* storage blocked: lasts for this visit */ } };

    const fold = root.querySelector("[data-ds-side-fold]");
    const mini = (on, keep) => {
      root.classList.toggle("ds-side-mini", on);
      if (fold) fold.setAttribute("aria-expanded", String(!on));
      if (keep) set("side.mini", on ? "1" : "0");
    };
    mini(get("side.mini") === "1");
    if (fold) fold.addEventListener("click", () => { const on = !root.classList.contains("ds-side-mini"); mini(on, true); if (on) fold.blur(); });

    const opener = root.querySelector("[data-ds-side-open]"), scrim = root.querySelector("[data-ds-scrim]");
    const drawer = (on) => {
      root.classList.toggle("ds-side-open", on);
      if (scrim) scrim.hidden = !on;
      if (opener) opener.setAttribute("aria-expanded", String(on));
    };
    if (opener) opener.addEventListener("click", () => drawer(true));
    if (scrim) scrim.addEventListener("click", () => drawer(false));
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && root.classList.contains("ds-side-open")) drawer(false); });
    root.querySelectorAll(".ds-side .ds-side-link").forEach((l) => l.addEventListener("click", () => drawer(false)));

    const buttons = [...root.querySelectorAll("[data-ds-theme]")];
    const theme = (t, keep) => {
      if (t !== "light" && t !== "dark") t = "auto";
      if (t === "auto") delete html.dataset.theme; else html.dataset.theme = t;
      buttons.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.dsTheme === t)));
      if (keep) set("theme", t);
    };
    if (buttons.length) { theme(get("theme")); buttons.forEach((b) => b.addEventListener("click", () => theme(b.dataset.dsTheme, true))); }
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
