// Design-system app shell (Camp de Base's side menu, made generic): fold the side menu to icons (kept per app), open it
// as a drawer on phones, the theme switch (Auto · Light · Dark), and full screen for any card, chart or map (v1.6).
// Copy it next to the app's pages and load it after the markup (SKILL.md › Shell, Full screen). It only toggles classes
// and attributes; every text lives in the HTML.
// Markup: a root with data-ds-shell (else <body>) and data-ds-app="<app>" (storage keys <app>.side.mini, <app>.theme),
// .ds-side-fold[data-ds-side-fold] in .ds-side-brand, [data-ds-side-open] in .ds-mtop, .ds-scrim[data-ds-scrim],
// theme buttons [data-ds-theme="auto|light|dark"] in .ds-side-foot.
// Full screen: button.ds-fs-btn[data-ds-fs] inside the card ([data-ds-fs-card], else the closest .ds-panel / .ds-card);
// the card gets .ds-full and fires "ds-fullscreen" (detail {on, settled}) right away and once the window has settled,
// so the app redraws its chart at the new size (a window "resize" is fired too, for maps).
// Filter bar (v1.7): button[data-ds-filters-toggle] inside a .ds-filters folds or opens its controls on phones.
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
    root.addEventListener("click", (e) => { if (e.target.closest(".ds-side .ds-side-link")) drawer(false); }); // also links rendered later

    const buttons = [...root.querySelectorAll("[data-ds-theme]")];
    const theme = (t, keep) => {
      if (t !== "light" && t !== "dark") t = "auto";
      if (t === "auto") delete html.dataset.theme; else html.dataset.theme = t;
      buttons.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.dsTheme === t)));
      if (keep) set("theme", t);
    };
    if (buttons.length) { theme(get("theme")); buttons.forEach((b) => b.addEventListener("click", () => theme(b.dataset.dsTheme, true))); }

    // Filter bar (v1.7): on phones the « Filters » button opens or folds the controls of its .ds-filters (delegated,
    // so bars drawn later work too); the app keeps the count, data-on and the reset.
    document.addEventListener("click", (e) => {
      const b = e.target.closest("[data-ds-filters-toggle]"), bar = b && b.closest(".ds-filters");
      if (!bar) return;
      const on = b.getAttribute("aria-expanded") !== "true";
      b.setAttribute("aria-expanded", String(on));
      bar.classList.toggle("ds-filters--open", on);
    });

    // Full screen (Camp de Base's setFullscreen): the card covers the window, and the screen when the browser allows
    // it; refused (an iframe, an iPhone) the card still fills its frame. Esc, the button again, or leaving the
    // browser's full screen exits. One card at a time; delegated, so cards drawn later work too.
    let full = null;
    const cardOf = (b) => b.closest("[data-ds-fs-card]") || b.closest(".ds-panel, .ds-card");
    const fire = (card, on, settled) => {
      card.dispatchEvent(new CustomEvent("ds-fullscreen", { bubbles: true, detail: { on, settled } }));
      if (settled) window.dispatchEvent(new Event("resize"));
    };
    const fs = (card, on) => {
      if (!card || (on && full === card) || (!on && full !== card)) return;
      if (on && full) fs(full, false);
      full = on ? card : null;
      card.classList.toggle("ds-full", on);
      html.classList.toggle("ds-noscroll", on);
      card.querySelectorAll("[data-ds-fs]").forEach((b) => {
        if (b.dataset.dsFsTitle == null) b.dataset.dsFsTitle = b.title || "Full screen";
        b.setAttribute("aria-pressed", String(on));
        b.title = on ? (b.dataset.dsFsExitTitle || "Exit full screen (Esc)") : b.dataset.dsFsTitle;
      });
      try {
        if (on && document.fullscreenEnabled && !document.fullscreenElement) html.requestFullscreen?.().catch(() => {}); // not in a frame that forbids it
        if (!on && document.fullscreenElement) document.exitFullscreen?.().catch(() => {});
      } catch { /* refused: the CSS full screen stays */ }
      fire(card, on, false);
      setTimeout(() => { if ((full === card) === on) fire(card, on, true); }, 450); // after the browser's own switch
    };
    document.addEventListener("click", (e) => { const b = e.target.closest("[data-ds-fs]"); if (b) fs(cardOf(b), b.getAttribute("aria-pressed") !== "true"); });
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && full && !document.querySelector("dialog[open]")) fs(full, false); });
    document.addEventListener("fullscreenchange", () => { if (!document.fullscreenElement && full) fs(full, false); });
    window.addEventListener("hashchange", () => { if (full && !full.isConnected) { html.classList.remove("ds-noscroll"); full = null; } });
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
