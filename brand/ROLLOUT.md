# Brand Look Rollout — every repo & website

How we take the canonical brand (defined in this `brand/` directory) and turn it on
everywhere. The model is **hub-and-spoke**: this profile repo is the hub (source of
truth); every other repo and site is a spoke that references the hub's tokens, CSS, and
SVG assets via raw-GitHub URLs. No build step, no cloud service, no copies to keep in sync.

> **Access note.** A single automation session is usually scoped to one repo at a time, so
> the spokes are rolled out repo-by-repo (each as its own PR). This file is the script for
> each of those PRs — apply the relevant section, check the box, move on.

---

## What "enabling the brand look" means per surface

| Surface | Action |
|---------|--------|
| **A repo README** | Paste `snippets/readme-header.md` masthead + covenant footer; convert badges to the `badges-and-stats.md` recipe. |
| **A website (GitHub Pages / domain)** | Add `snippets/site-head.html` to `<head>`; restyle with `var(--…)` from `brand.css`; use `--grad-surface` bg + `bard-wordmark` headings. |
| **GitHub stat cards** | Replace theme params with the `badges-and-stats.md` strings. |
| **Social / OG images** | Point `og:image` at the canonical `assets/banner.svg` (or a per-repo SVG built from the shared `<defs>`). |
| **HuggingFace / external profiles** | Reuse `assets/logo.svg` + covenant tagline + palette. |

## The reference assets (the hub)

- Tokens: `brand/tokens.json` · CSS: `brand/brand.css` · Guide: `brand/BRAND.md`
- SVGs: `assets/banner.svg`, `assets/logo.svg`, `assets/space-pipeline.svg`, `assets/maglev-tube.svg`
- Raw base URL: `https://raw.githubusercontent.com/thebardchat/thebardchat/main/`

---

## Rollout waves

Order by visibility so the most-seen surfaces land first.

### Wave 0 — Hub (this repo) ✅ in progress
- [x] `brand/tokens.json`, `brand/brand.css`, `brand/BRAND.md`, snippets
- [ ] Optional: add a "Brand Kit" link to the profile README

### Wave 1 — Flagship sites (highest traffic)
- [ ] `thebardchat.github.io` (showcase)
- [ ] `BGKPJR-Launch-Vis` (site + README) — already Astro/Svelte, wire `brand.css` vars
- [ ] `manna-pods` (site + README)
- [ ] `mega-crew-stories` (saga site + `mega.shanebrain.cloud`)

### Wave 2 — Aerospace repos
- [ ] `manna` · `BGKPJR-Core-Simulations` · `tug-pro` — README headers + badges

### Wave 3 — Platform / product repos
- [ ] `shanebrain_mcp` · `angel-cloud` · `pulsar_sentinel` · `thought-tree`
- [ ] `AI-Trainer-MAX` · `srm-dispatch` · `mini-shanebrain`

### Wave 4 — Archive / long-tail
- [ ] `angelcloud-actual` · `treasures` · `you-probably-think-this-book-is-about-you`
- [ ] `constitution` (keep text-forward; header + footer only)

### Wave 5 — External profiles
- [ ] HuggingFace `thebardchat` · Twitch channel art · Amazon author/book page

> Update the boxes as each PR merges. The repo list is derived from the profile README's
> "What's Live", "Released Treasures", and BGKPJR tables — add new repos here as they ship.

---

## Per-repo procedure (copy into each spoke PR)

1. **README** — paste the masthead from `snippets/readme-header.md`, set `REPO_NAME` + tagline,
   convert badges using `snippets/badges-and-stats.md`, add the covenant footer.
2. **Site (if any)** — add `snippets/site-head.html` to `<head>`. Replace hard-coded colors
   with `var(--…)`; set `body { background: var(--grad-surface); font-family: var(--font-sans); }`.
3. **Stat cards** — swap theme params to the canonical strings.
4. **Verify** (see below), commit on a branch, open a **draft PR**, link back to this file.

## Verification

- **Tokens valid:** `python -c "import json; json.load(open('brand/tokens.json'))"` → no error.
- **README renders:** preview on GitHub (or `grip`); banner + badges load, no broken images.
- **Site:** open the page; confirm `brand.css` loads (Network tab 200), background uses
  `--grad-surface`, headings show the cyan→amber wordmark, links are cyan. Check mobile width.
- **Palette parity:** spot-check against `BRAND.md` — no off-palette hex, fonts resolve to
  Space Grotesk / JetBrains Mono.
- **A11y:** body text on `--surface-void` should be `--text-dim` or lighter for contrast.

## Keeping it in sync

Because spokes reference the hub by URL, a token change here propagates on next load — so
**bump `version`** in `tokens.json` + `brand.css` and note it below. Sites that vendored a
copy re-pull on their own cadence.

### Changelog
- **1.0.0** (2026-06-29) — Initial brand kit extracted from `assets/*.svg` and profile badges.
