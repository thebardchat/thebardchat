# thebardchat — Brand Look

**The single source of truth for the visual identity of the thebardchat / ShaneBrain ecosystem.**
Every repo and website should derive its look from the tokens here — never hand-pick new
colors or fonts. If a value isn't in [`tokens.json`](./tokens.json), it isn't on-brand yet.

Machine-readable tokens: [`tokens.json`](./tokens.json) · Drop-in stylesheet: [`brand.css`](./brand.css) · Rollout steps: [`ROLLOUT.md`](./ROLLOUT.md)

---

## The look in one line

Deep-space technical drawing: near-black navy surfaces, a faint blueprint grid, a
**cyan → amber** signature gradient, post-quantum violet and a covenant green, set in
**Space Grotesk** display + **JetBrains Mono** technical type, with corner brackets, a
starfield, and soft glow.

---

## Color

| Role | Token | Hex | Use |
|------|-------|-----|-----|
| **Primary** | `brand.cyan` | `#00e5ff` | Links, headings, glow, primary accent |
| | `brand.cyan-light` | `#7ee8ff` | Gradient partner / hover |
| **Secondary** | `brand.amber` | `#ffaa00` | CTAs, highlights, readouts |
| | `brand.amber-light` | `#ffd066` | Gradient partner / hover |
| **Accent** | `brand.violet` | `#7c3aed` | Stats icons, fire, post-quantum |
| | `brand.violet-light` | `#a78bfa` | Gradient partner / hover |
| **Covenant** | `brand.green` | `#b4ff6e` | Tagline, success, faith line |
| Surface | `surface.void` | `#040910` | Darkest background |
| Surface | `surface.deep` | `#070f1c` | Background gradient stop |
| Surface | `surface.panel` | `#0a1422` | Cards / panels |
| Surface | `surface.github` | `#0d1117` | shields.io + stat-card backgrounds |
| Structure | `structure.grid-minor` | `#192e4c` | 50px grid |
| Structure | `structure.grid-major` | `#254469` | 250px grid / borders |
| Structure | `structure.steel` | `#4a6e96` | Hardware line work |
| Text | `text.white` `#ffffff` · `text.bright` `#ddeeff` · `text.dim` `#8faec8` · `text.muted` `#4d6680` | | bright→muted hierarchy |

**Signature gradient** (the wordmark): `#00e5ff → #7ee8ff → #ffaa00` at ~105°.

## Typography

| Role | Stack | Notes |
|------|-------|-------|
| Display | `'Space Grotesk', 'Inter', 'Helvetica Neue', sans-serif` | weight **700**, letter-spacing **-0.03em** |
| Body | `'Inter', 'Helvetica Neue', sans-serif` | |
| Mono | `'JetBrains Mono', 'Fira Code', 'Courier New', monospace` | readouts, labels, taglines (letter-spacing ~0.32em) |

## Motifs (what makes an asset feel on-brand)

`corner-brackets` · `starfield` · `scan-line` · `technical-grid` · `radial-halo` · `glow-merge`

Reference implementations live in the SVGs in [`/assets`](../assets): `banner.svg`, `logo.svg`,
`space-pipeline.svg`, `maglev-tube.svg`. Copy their `<defs>` (gradients, filters, grid patterns)
rather than reinventing — they are the canonical expression of every token above.

## Voice (so copy matches the look)

Tagline lockup: **FAITH · FAMILY · SOBRIETY · LOCAL AI · LEFT-BEHIND USER**
Locator: **HAZEL GREEN, ALABAMA · ZERO CLOUD**. Plain, honest, mission-first. "Shane is the
vision. Claude is the velocity." Never "one guy built this."

## Do / Don't

- ✅ Reference `tokens.json` / `brand.css`; pin the version.
- ✅ Reuse the SVG `<defs>` for gradients, glow filters, and the grid.
- ✅ Keep shields.io badges on `bg`/`label` = `0d1117` with cyan/amber/violet accents.
- ❌ Don't introduce off-palette colors or swap the font stacks.
- ❌ Don't bake the wordmark gradient as a flat color.
- ❌ Don't recolor the covenant green — it's reserved for the tagline/faith line.

## Versioning

Bump `version` in `tokens.json` (and the header in `brand.css`) on any token change, and note
it in [`ROLLOUT.md`](./ROLLOUT.md). Downstream consumers pin to a version so changes are opt-in.
