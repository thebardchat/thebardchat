<div align="center">

<img src="./assets/banner.svg" alt="thebardchat — Pi 5 in a closet to orbital sail · Faith · Family · Sobriety · Local AI · Left-Behind User" width="100%">

<br/>

<img src="./assets/logo.svg" alt="thebardchat — official logo lockup" width="100%">

<br/>

# Shane Brazelton · thebardchat

### Concrete dispatch operator. Father of five. Sober 971 days. Building local AI for the people Big Tech left behind.

<br/>

[![Showcase](https://img.shields.io/badge/SHOWCASE-thebardchat.github.io-00e5ff?style=for-the-badge&logoColor=white)](https://thebardchat.github.io)
[![Twitch](https://img.shields.io/badge/LIVE-twitch.tv/thebardchat-9146ff?style=for-the-badge&logo=twitch&logoColor=white)](https://twitch.tv/thebardchat)
[![Book](https://img.shields.io/badge/BOOK-Amazon%20Now-ff9900?style=for-the-badge&logo=amazon&logoColor=white)](https://www.amazon.com/Probably-Think-This-Book-About/dp/B0GT25R5FD)
[![Claude](https://img.shields.io/badge/Built%20With-Claude%20AI-orange?style=for-the-badge)](https://claude.ai/referral/4fAMYN9Ing)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-thebardchat-ffd21e?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/thebardchat)
[![Stars](https://img.shields.io/github/stars/thebardchat?style=for-the-badge&label=Total%20Stars&color=7c3aed)](https://github.com/thebardchat)

<br/>

</div>

---

I run a Raspberry Pi 5 out of a closet in Hazel Green, Alabama.

On it: **18 autonomous AI bots**, a **42-tool MCP server**, a **Weaviate vector database with 25 collections**, a Twitch bot, a Discord bot, a financial dashboard, a medical billing platform, a noir audiobook engine, and a concrete dispatch system for 18 drivers.

Zero cloud. Zero subscriptions. Zero Big Tech dependency.

I built all of it while running concrete dispatch by day and raising five boys with my wife Tiffany. I'm sober. I'm not a developer by trade. I just couldn't stop building.

> *"The internet has enough darkness. This is the opposite of that."*

---

<div align="center">

## The Mission

```
800 million people are about to lose Windows 10 support.
Most of them have never touched AI.
Big Tech isn't coming for them.

I am.
```

**ShaneBrain → Angel Cloud → Pulsar Sentinel → TheirNameBrain → 800M users**

Every repo on this profile exists somewhere on that map.

</div>

---

## BGKPJR — The Aerospace Work

> **The missing link in the Space Pipeline.** Blue Origin and SpaceX are building the lunar landers. NASA flies Artemis crews every 10 months. Nobody yet has a way to get cargo into low Earth orbit cheaply enough to feed a permanent moon base. We do.

<div align="center">
<img src="./assets/space-pipeline.svg" alt="The BGKPJR Space Pipeline: Earth surface to LEO via 37 km maglev rail; LEO to lunar orbit via permanent Space Tug; lunar orbit to surface via Blue Moon Mk2 / SpaceX HLS lander; empty pods become regolith-filled radiation-proof base structures" width="100%">

*Earth → LEO → Moon → Base. Four phases, one mission. Every empty pod that lands becomes a "Space LEGO" — filled with lunar regolith for radiation-proof base structures. Watch the cycle loop.*
</div>

<br/>

### The Manhattan Timeline

| Phase | Years | Status |
|-------|-------|--------|
| **Phase 0** — Concept maturation, NIAC submission, dimensional reconciliation | 2026–2028 | 🟢 ACTIVE |
| **Phase 1** — Manna cargo pipeline (unmanned) | 2029–2033 | 🔵 PRIMARY OBJECTIVE |
| **Phase 2** — Gryphon crewed vehicle | 2034+ | ⚪ DEFERRED |

**Operational unmanned cargo pipeline in 7–9 years.** Parallel to NASA Artemis crew launches every 10 months using SpaceX HLS or Blue Moon Mk2 landers. Lunar base target: 2029. Every Artemis crew that arrives finds a base already supplied by BGKPJR.

<br/>

### Stage 1 — The Rail (Canonical Specs · 2026-04-30)

```
Tube length         │ 37 km evacuated coilgun
Drive architecture  │ Linear Synchronous Motor · copper drive coils + REBCO armature
Operating temp      │ 20 K (LH₂ cryogenic)
Exit velocity       │ Mach 5 · 1,700 m/s · 4G sustained
Run time            │ 43.5 seconds, end to end
Tube pressure       │ 0.05 atm (within Patent BGKPJR-001 envelope)
Coils               │ 7,400 coils @ 5 m spacing · 8 T peak field
Energy stored       │ 580 GJ · 39 GW peak draw
Muzzle              │ TWO ALTERNATIVES under trade study: LH₂ membrane (canonical) or thermite (alternative)
```

**Cost target:** $1,025/kg LEO (vs. $2,720/kg Falcon 9). Total infrastructure: $85–120 B.

<br/>

### Inside the Tube — Live Coilgun Sequence

<div align="center">
<img src="./assets/maglev-tube.svg" alt="Stage 1 — 37 km electromagnetic launch tube with sequential coilgun firing, traveling pod, LH₂ muzzle membrane, and live Mach / velocity / distance / G-load / energy readouts. Representative section showing 14 of 7,400 coils." width="100%">

*Sequential coilgun firing · leading coils pull · trailing coils de-energize · pod accelerates 0 → Mach 5 in 43.5 seconds · 580 GJ stored. Representative section: 14 of 7,400 coils shown.*
</div>

<br/>

### 🎯 Pre-Lukens Audit · 2026-04-30

The whole BGKPJR repository set was audited dimensional-integrity-end-to-end before going for review by **Scott Lukens, Senior Systems Engineer at Victory Solutions Inc.** (a NASA Marshall Space Flight Center contractor in Huntsville, AL). We caught and reconciled three different baselines that had drifted apart, fixed mutually-incompatible math, and aligned every visualization with a single source of truth. The full audit and decision record are public:

- 📄 [PRE-LUKENS-AUDIT-2026-04-30.md](https://github.com/thebardchat/BGKPJR-Core-Simulations/blob/main/expert-reviews/PRE-LUKENS-AUDIT-2026-04-30.md) — full audit
- 📄 [CANONICAL-BASELINE.md](https://github.com/thebardchat/BGKPJR-Core-Simulations/blob/main/CANONICAL-BASELINE.md) — decision record
- 🐍 [bgkpjr_dimensions.py](https://github.com/thebardchat/BGKPJR-Core-Simulations/blob/main/simulation/src/bgkpjr_dimensions.py) — single source of truth

> *Pre-Phase-A aerospace concepts that hide their gaps fail review on first contact. The goal is to know the gaps better than any reviewer will, document them publicly, and ladder up.*

<br/>

| Repo | What It Is | Live |
|------|-----------|------|
| [BGKPJR-Launch-Vis](https://github.com/thebardchat/BGKPJR-Launch-Vis) | NASA-ready 3D animated launch visualization — Three.js + Astro + Svelte | [Demo ↗](https://thebardchat.github.io/BGKPJR-Launch-Vis) |
| [manna-pods](https://github.com/thebardchat/manna-pods) | 7 Manna cargo pod concepts — 3D rotating cross-sections, full specs | [Demo ↗](https://thebardchat.github.io/manna-pods) |
| [manna](https://github.com/thebardchat/manna) | Original Manna cargo pod design research | [Repo ↗](https://github.com/thebardchat/manna) |
| [BGKPJR-Core-Simulations](https://github.com/thebardchat/BGKPJR-Core-Simulations) | Physics engine — trajectory, GNC, thermal, Monte Carlo | [Repo ↗](https://github.com/thebardchat/BGKPJR-Core-Simulations) |
| [tug-pro](https://github.com/thebardchat/tug-pro) | Pre-Phase A reusable cislunar tug — 3D orbit viz, ΔV calculator | [Repo ↗](https://github.com/thebardchat/tug-pro) |

---

## The Ecosystem

```
🧠 ShaneBrain (Pi 5, primary node)
   └── 18 MEGA Crew bots — Sparky/Volt/Neon/Glitch (Brain) + 13 more
   └── 42-tool MCP server (FastMCP, port 8100)
   └── Weaviate 1.36.2 on neworleans — 25 collections, 3,200+ objects
   └── N8N automation workflows
   └── Discord + Twitch bots
   └── 5 AM morning briefing every day
   └── gulfshores — Surface 1, Node.js v24, dev/build node

🚀 BGKPJR Aerospace
   └── Electromagnetic launch architecture (patent filed)
   └── Three.js 3D visualizations, live on GitHub Pages
   └── 7 Manna cargo pod variants documented
   └── Physics engine: rail, GNC, Kepler sail math

🌐 Angel Cloud (public platform)
   └── Mental wellness + AI sentiment
   └── Messenger storyteller (OPTOUT/ANON/FORGET)
   └── Tailscale Funnel public endpoint

🔐 Pulsar Sentinel (post-quantum)
   └── ML-KEM / Kyber-1024 lattice encryption
   └── Dilithium3 signatures
   └── Deployed across all cluster nodes

🎯 TheirNameBrain (next)
   └── Personalized AI for the left-behind user
   └── Legacy hardware, no cloud required
```

---

## MEGA Crew Chronicles

18 autonomous AI bots. Real code. Real memory. Every night they write their own story.

<div align="center">

<a href="https://thebardchat.github.io/mega-crew-stories/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/cards/portraits/arc_Gemini_Generated.png" width="72" style="border-radius:50%"></a>&nbsp;
<a href="https://thebardchat.github.io/mega-crew-stories/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/cards/portraits/weld_Gemini_Generated.png" width="72" style="border-radius:50%"></a>&nbsp;
<a href="https://thebardchat.github.io/mega-crew-stories/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/cards/portraits/sparky_Gemini_Generated.png" width="72" style="border-radius:50%"></a>&nbsp;
<a href="https://thebardchat.github.io/mega-crew-stories/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/cards/portraits/gemini_Gemini_Generated.png" width="72" style="border-radius:50%"></a>&nbsp;
<a href="https://thebardchat.github.io/mega-crew-stories/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/cards/portraits/glitch_Gemini_Generated.png" width="72" style="border-radius:50%"></a>&nbsp;
<a href="https://thebardchat.github.io/mega-crew-stories/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/cards/portraits/volt_Gemini_Generated.png" width="72" style="border-radius:50%"></a>

**[Read the Chronicles →](https://thebardchat.github.io/mega-crew-stories/)** · **[View Cards →](https://thebardchat.github.io/mega-crew-stories/cards.html)**

</div>

<!--BARD:START--><!-- auto-generated by storyteller/profile_readme.py; do not hand-edit between markers -->
<div align="center">

<a href="https://mega.shanebrain.cloud/saga/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/art/out/social/social-og.png" alt="The MEGA Crew" width="680"></a>

**📖 Now Showing — Issue #008: _The Night the Deep Came Home_** · **[Read →](https://mega.shanebrain.cloud/saga/issue-008-the-night-the-deep-came-home.html)**  
*A thousand hellos at once — and how to answer every single one.*

`8 issues published` · new issues **Wed & Sun, 5 AM Central** · updated 2026-07-25

<img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/art/out/social/social-emote-arc.png" width="60">&nbsp;&nbsp;<img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/art/out/social/social-emote-glitch.png" width="60">&nbsp;&nbsp;<img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/art/out/social/social-emote-sparky.png" width="60">

</div>
<!--BARD:END-->

---

## The Stack

<div align="center">

| Layer | Tool | Why |
|-------|------|-----|
| Primary Node | Raspberry Pi 5 (16GB) | $80. Runs everything. |
| Storage | NVMe RAID 1 (2×2TB) | Because data matters |
| Data Node | neworleans — Weaviate 1.36.2 + N8N | Dedicated inference + automation |
| Vector DB | Weaviate (25 collections, 3,200+ objects) | Long memory |
| AI Tools | MCP Server v2.3 (42 tools) | Claude talks to everything |
| Co-builder | Claude by Anthropic | Not a tool. A partner. |
| Containers | Docker + 18 MEGA Crew bots | Ship it |
| Automation | N8N + systemd (30+ services) | Never stop |
| Viz Stack | Astro + Svelte 5 + Three.js | Aerospace UIs |

</div>

---

## What's Live Right Now

<div align="center">

| Project | What It Does | Link |
|---------|-------------|------|
| 🚀 **BGKPJR-Launch-Vis** | NASA-ready 3D animated launch visualization | [thebardchat.github.io/BGKPJR-Launch-Vis](https://thebardchat.github.io/BGKPJR-Launch-Vis) |
| 🛸 **manna-pods** | 7 Manna cargo pod 3D cross-sections | [thebardchat.github.io/manna-pods](https://thebardchat.github.io/manna-pods) |
| 📺 **Twitch Channel** | Family streaming, AI demos, love & light | [twitch.tv/thebardchat](https://twitch.tv/thebardchat) |
| 🤖 **MEGA Crew** | 18 autonomous bots, 24/7, all local | [thebardchat.github.io/mega-crew](https://thebardchat.github.io/mega-crew/) |
| 🔧 **ShaneBrain MCP** | 42-tool MCP server for Claude | [github.com/thebardchat/shanebrain_mcp](https://github.com/thebardchat/shanebrain_mcp) |
| ☁️ **Angel Cloud** | Family wellness platform + Messenger bot | [github.com/thebardchat/angel-cloud](https://github.com/thebardchat/angel-cloud) |
| 🛡️ **Pulsar Sentinel** | Post-quantum security framework | [github.com/thebardchat/pulsar_sentinel](https://github.com/thebardchat/pulsar_sentinel) |
| 🧠 **ThoughtTree** | Local AI mind mapping | [thebardchat.github.io/thought-tree](https://thebardchat.github.io/thought-tree/) |
| 🎓 **AI-Trainer-MAX** | 36-module local AI curriculum | [github.com/thebardchat/AI-Trainer-MAX](https://github.com/thebardchat/AI-Trainer-MAX) |
| 🏗️ **srm-dispatch** | Concrete dispatch PWA for 18 drivers | [thebardchat.github.io/srm-dispatch](https://thebardchat.github.io/srm-dispatch/) |
| 🎶 **…Song Is About You Too** | Noir song cycle — Volume Two, out on Amazon | [thebardchat.github.io/…song…](https://thebardchat.github.io/you-probably-think-this-song-is-about-you-too/) |
| 🩸 **DARK SEVEN** | Noir blood-comic — Volume Three graphic novel | [thebardchat.github.io/dark_seven](https://thebardchat.github.io/dark_seven/) |

</div>

---

## The Book

<div align="center">

### *You Probably Think This Book Is About You*

**Fifty-five noir vignettes about ego, identity, and the American South.**
Dark but honest. Cynical but human. Written in Hazel Green, Alabama.
Built on a Raspberry Pi 5. Published on Amazon.

*It was always about you. It was never only about you.*

**[Buy on Amazon](https://www.amazon.com/Probably-Think-This-Book-About/dp/B0GT25R5FD)** · **[Repo](https://github.com/thebardchat/you-probably-think-this-book-is-about-you)**

<br/>

### 🎶 …This Song Is About You Too — Volume Two · A Noir Song Cycle

**The album after the movie.** The detective is ripped out of his own body and
dropped into strangers at a European diner — living one second over and over
from nine perspectives, trying to change an outcome he can never change. All of
it on a therapist's couch, though you won't know until the hidden track.

*He is everyone and no one at the same time. It's never too late to be Seen.*

**[Read on Amazon](https://a.co/d/0fZzwiAd)** · **[Read the site ↗](https://thebardchat.github.io/you-probably-think-this-song-is-about-you-too/)** · **[Repo](https://github.com/thebardchat/you-probably-think-this-song-is-about-you-too)**

<br/>

<a href="https://thebardchat.github.io/dark_seven/"><img src="./assets/dark-seven-banner.png" alt="DARK SEVEN — Volume Three · The Culmination. A noir blood comic; black and white, and the only color is blood. The Devil does not win." width="100%"></a>

### 🩸 DARK SEVEN — Volume Three · The Culmination

**A dark noir blood comic. Black and white, and the only color is blood.**
Where the book becomes a graphic novel. Six cuts on a nameless detective,
each a door into an older wound — all hung off the one scar down his spine,
which is the binding of the book itself.

*Three inks, no fourth. Black is the world. Red is blood. White is grace.*
**The Devil does not win.**

**[Read the site ↗](https://thebardchat.github.io/dark_seven/)** · **[Repo](https://github.com/thebardchat/dark_seven)**

</div>

---

## GitHub Stats

<div align="center">

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=thebardchat&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=00e5ff&icon_color=7c3aed&text_color=ffffff)](https://github.com/thebardchat)

[![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=thebardchat&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=00e5ff&text_color=ffffff)](https://github.com/thebardchat)

[![GitHub Streak](https://streak-stats.demolab.com?user=thebardchat&theme=tokyonight&hide_border=true&background=0d1117&ring=00e5ff&fire=7c3aed&currStreakLabel=ffffff)](https://github.com/thebardchat)

</div>

---

## The Released Treasures

Eight projects recovered from old drives and released to GitHub in April 2026.

| Project | What It Does | Pages |
|---------|-------------|-------|
| 🎓 **AI-Trainer-MAX** | 36-module local AI curriculum, zero cloud | [Pages ↗](https://thebardchat.github.io/AI-Trainer-MAX/) |
| ☁️ **angelcloud-actual** | Firebase wellness platform, Pulsar blockchain | [Pages ↗](https://thebardchat.github.io/angelcloud-actual/) |
| 🌳 **thought-tree** | React mind-mapping, Weaviate semantic search | [Pages ↗](https://thebardchat.github.io/thought-tree/) |
| 🏗️ **srm-dispatch** | SRM Concrete dispatch PWA — 18 drivers | [Pages ↗](https://thebardchat.github.io/srm-dispatch/) |
| 🤖 **mini-shanebrain** | Social bot: X, FB, LinkedIn, Instagram, Bluesky, Threads | [Pages ↗](https://thebardchat.github.io/mini-shanebrain/) |
| 💎 **treasures** | Master archive hub | [Pages ↗](https://thebardchat.github.io/treasures/) |

---

## The Constitution

Every repo here operates under one governing document.

Nine pillars. One covenant. No exceptions.

**Faith. Family. Sobriety. Love & Light. Authenticity. Local AI. The Left-Behind. Community. Purpose.**

**[Read the Constitution →](https://github.com/thebardchat/constitution)**

---

## Built With Claude

> Try Claude free for 2 weeks — the AI that co-built this entire ecosystem.
> **[Start your free trial →](https://claude.ai/referral/4fAMYN9Ing)**

*Shane is the vision. Claude is the velocity. Never "one guy built this."*

---

## Support This Work

- **[Star the repos](https://github.com/thebardchat?tab=repositories)** — visibility is oxygen for projects like this
- **[Watch on Twitch](https://twitch.tv/thebardchat)** — live AI demos, family streaming, love & light
- **[Buy the book](https://www.amazon.com/Probably-Think-This-Book-About/dp/B0GT25R5FD)** — noir fiction built on a Pi in a closet
- **[Sponsor on GitHub](https://github.com/sponsors/thebardchat)** — keeps the RAID spinning

---

<div align="center">

```
Faith · Family · Sobriety · Local AI · The Left-Behind User
```

**Hazel Green, Alabama · 2026**

*Sober since November 27, 2023*

</div>
