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
// Filter bar (v1.7): button[data-ds-filters-toggle] inside a .ds-filters folds or opens its controls on phones (on every
// screen with .ds-filters--fold, v1.7.1).
// App switcher (v1.9): <div class="ds-apps" data-ds-apps></div> right under .ds-side-brand; filled from the registry
// apps.json (inline <script type="application/json" id="ds-apps-data">, else fetched from data-ds-apps-src, default
// "apps.json" next to the page). Names and links come from the registry, the icons from the kit (":ci-name:" tokens).
// The current app is the entry whose host is this page's, else whose "shell" equals data-ds-app.
// Help mark (v1.10): button.ds-help[data-ds-help="plain-language text"] beside a chart or KPI title; a tap or click
// opens the text in one .ds-help-pop under the mark (works on touch screens, where a title never shows).
// Sheet (v1.11): window.DSSheet.open(sheet, opener) shows an aside.ds-sheet and the .ds-sheet-scrim right before it,
// keeps Tab inside, closes on Esc, on a click on the scrim or a [data-ds-sheet-close] button, then gives the focus back
// to the opener; the sheet fires "ds-sheet" (detail {open}) so the app can keep its state (e.g. the URL).
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
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !e.defaultPrevented && root.classList.contains("ds-side-open")) drawer(false); });
    root.addEventListener("click", (e) => { if (e.target.closest(".ds-side .ds-side-link")) drawer(false); }); // also links rendered later

    const buttons = [...root.querySelectorAll("[data-ds-theme]")];
    const theme = (t, keep) => {
      if (t !== "light" && t !== "dark") t = "auto";
      if (t === "auto") delete html.dataset.theme; else html.dataset.theme = t;
      buttons.forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.dsTheme === t)));
      if (keep) set("theme", t);
    };
    if (buttons.length) { theme(get("theme")); buttons.forEach((b) => b.addEventListener("click", () => theme(b.dataset.dsTheme, true))); }

    // App switcher (v1.9): one registry (apps.json), one menu for every app.
    const appsBox = root.querySelector("[data-ds-apps]");
    const esc = (t) => String(t ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
    const drawApps = (reg) => {
      const list = (reg && reg.apps) || [];
      if (!appsBox || !list.length) return;
      const host = location.hostname;
      const hostOf = (u) => { try { return new URL(u).hostname; } catch { return ""; } };
      const cur = list.find((a) => host && hostOf(a.url) === host && a.kind !== "hub") || list.find((a) => a.shell === app) || null;
      const item = (a) => `<a href="${esc(a.url)}" data-ds-apps-key="${esc(a.key)}"${a === cur ? ' aria-current="true"' : ' target="_top"'}>` +
        `<span class="ico">:ci-${esc(a.icon || "other")}:</span><span>${esc(a.name)}${a.note ? `<br><small>${esc(a.note)}</small>` : ""}</span>` +
        `<span class="ds-count" data-ds-apps-count="${esc(a.key)}"></span></a>`;
      const apps = list.filter((a) => a.kind !== "hub"), hubs = list.filter((a) => a.kind === "hub");
      appsBox.innerHTML = `<button type="button" class="ds-apps-btn" aria-haspopup="true" aria-expanded="false" title="Changer d'app">` +
        `<span class="ico">:ci-${esc((cur && cur.icon) || "home")}:</span><span class="ds-apps-name">${esc(cur ? cur.name : "Apps")}</span>` +
        `<span class="ds-apps-caret" aria-hidden="true">⌄</span></button>` +
        `<div class="ds-apps-menu" hidden>${apps.map(item).join("")}${hubs.length ? "<hr>" + hubs.map(item).join("") : ""}</div>`;
      const btn = appsBox.querySelector(".ds-apps-btn"), menu = appsBox.querySelector(".ds-apps-menu");
      const open = (on) => { menu.hidden = !on; btn.setAttribute("aria-expanded", String(on)); };
      btn.addEventListener("click", () => open(menu.hidden));
      document.addEventListener("click", (e) => { if (!appsBox.contains(e.target)) open(false); });
      document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !menu.hidden) { open(false); btn.focus(); } });
      appsBox.dispatchEvent(new CustomEvent("ds-apps", { bubbles: true, detail: { apps: list, current: cur } }));
    };
    if (appsBox) {
      const inline = document.getElementById("ds-apps-data");
      if (inline) { try { drawApps(JSON.parse(inline.textContent)); } catch { /* bad registry: no switcher */ } }
      else fetch(appsBox.dataset.dsAppsSrc || "apps.json", { credentials: "same-origin" }).then((r) => (r.ok ? r.json() : null)).then(drawApps).catch(() => {});
    }

    // Filter bar (v1.7): on phones (every screen for .ds-filters--fold) the « Filters » button opens or folds the controls of its .ds-filters (delegated,
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
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !e.defaultPrevented && full && !document.querySelector("dialog[open]")) fs(full, false); });
    document.addEventListener("fullscreenchange", () => { if (!document.fullscreenElement && full) fs(full, false); });
    window.addEventListener("hashchange", () => { if (full && !full.isConnected) { html.classList.remove("ds-noscroll"); full = null; } });
  };
  // Help marks (v1.10): one popover for the page, opened by a tap or click on a .ds-help, closed by Esc, a tap elsewhere or scrolling.
  const helpStart = () => {
    let pop = null, owner = null;
    const close = () => { if (pop) pop.remove(); if (owner) owner.setAttribute("aria-expanded", "false"); pop = owner = null; };
    document.addEventListener("click", (e) => {
      const b = e.target.closest(".ds-help[data-ds-help]");
      if (!b) { if (pop && !e.target.closest(".ds-help-pop")) close(); return; }
      e.preventDefault(); e.stopPropagation();
      if (owner === b) { close(); return; }
      close();
      pop = document.createElement("div");
      pop.className = "ds-help-pop"; pop.setAttribute("role", "tooltip"); pop.id = "ds-help-pop"; pop.textContent = b.dataset.dsHelp;
      document.body.append(pop);
      const r = b.getBoundingClientRect(), w = pop.offsetWidth, h = pop.offsetHeight;
      const left = Math.max(16, Math.min(r.left + r.width / 2 - w / 2, innerWidth - w - 16));
      const top = r.bottom + 8 + h > innerHeight - 8 ? r.top - h - 8 : r.bottom + 8;
      pop.style.left = left + "px"; pop.style.top = Math.max(8, top) + "px";
      owner = b; b.setAttribute("aria-expanded", "true"); b.setAttribute("aria-describedby", "ds-help-pop");
    }, true);
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && pop) close(); });
    window.addEventListener("scroll", close, true); window.addEventListener("resize", close);
  };
  // Sheet (v1.11): one open at a time.
  let sheet = null, back = null;
  const focusables = (el) => [...el.querySelectorAll('a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])')]
    .filter((n) => n.offsetParent !== null || n === document.activeElement);
  const scrimOf = (el) => (el.previousElementSibling && el.previousElementSibling.classList.contains("ds-sheet-scrim") ? el.previousElementSibling : null);
  const closeSheet = () => {
    if (!sheet) return;
    const el = sheet, to = back;
    sheet = back = null;
    el.hidden = true; const s = scrimOf(el); if (s) s.hidden = true;
    if (!document.querySelector(".ds-full")) document.documentElement.classList.remove("ds-noscroll"); // a card may still be in full screen
    el.dispatchEvent(new CustomEvent("ds-sheet", { bubbles: true, detail: { open: false } }));
    if (to && to.isConnected && typeof to.focus === "function") to.focus();
  };
  const openSheet = (el, opener) => {
    if (!el) return;
    if (sheet && sheet !== el) closeSheet();
    if (!sheet) back = opener || document.activeElement;
    sheet = el; el.hidden = false; const s = scrimOf(el); if (s) s.hidden = false;
    document.documentElement.classList.add("ds-noscroll");
    const first = el.querySelector("[data-ds-sheet-close]") || focusables(el)[0];
    if (first) first.focus({ preventScroll: true });
    el.dispatchEvent(new CustomEvent("ds-sheet", { bubbles: true, detail: { open: true } }));
  };
  window.DSSheet = { open: openSheet, close: closeSheet, get current() { return sheet; } };
  document.addEventListener("click", (e) => {
    if (!sheet) return;
    if (e.target.closest("[data-ds-sheet-close]") || e.target.classList.contains("ds-sheet-scrim")) closeSheet();
  });
  document.addEventListener("keydown", (e) => {
    if (!sheet) return;
    if (e.key === "Escape" && !document.querySelector(".ds-help-pop")) { e.preventDefault(); closeSheet(); return; }
    if (e.key !== "Tab") return;
    const f = focusables(sheet); if (!f.length) return;
    const a = f[0], z = f[f.length - 1];
    if (e.shiftKey && (document.activeElement === a || !sheet.contains(document.activeElement))) { e.preventDefault(); z.focus(); }
    else if (!e.shiftKey && (document.activeElement === z || !sheet.contains(document.activeElement))) { e.preventDefault(); a.focus(); }
  });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", helpStart); else helpStart();
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
