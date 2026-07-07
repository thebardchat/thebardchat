<div align="center">

<img src="./assets/banner.svg" alt="thebardchat — Pi 5 in a closet to orbital sail · Faith · Family · Sobriety · Local AI · Left-Behind User" width="100%">

<br/>

<img src="./assets/logo.svg" alt="thebardchat — official logo lockup" width="100%">

<br/>

# Shane Brazelton · thebardchat

### Concrete dispatch operator. Father of five. Sober 953 days. Building local AI for the people Big Tech left behind.

<br/>

[![Showcase](https://img.shields.io/badge/SHOWCASE-thebardchat.github.io-00e5ff?style=for-the-badge&logoColor=white)](https://thebardchat.github.io)
[![Twitch](https://img.shields.io/badge/LIVE-twitch.tv/thebardchat-9146ff?style=for-the-badge&logo=twitch&logoColor=white)](https://twitch.tv/thebardchat)
[![Discord](https://img.shields.io/badge/DISCORD-Join%20the%20Crew-5865f2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/dTH2Uauhb4)
[![Book](https://img.shields.io/badge/BOOK-Amazon%20Now-ff9900?style=for-the-badge&logo=amazon&logoColor=white)](https://www.amazon.com/Probably-Think-This-Book-About/dp/B0GT25R5FD)
[![Claude](https://img.shields.io/badge/Built%20With-Claude%20AI-orange?style=for-the-badge)](https://claude.ai/referral/4fAMYN9Ing)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-thebardchat-ffd21e?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/thebardchat)
[![Stars](https://img.shields.io/github/stars/thebardchat?style=for-the-badge&label=Total%20Stars&color=7c3aed)](https://github.com/thebardchat)

<br/>

</div>

---

I run a Raspberry Pi 5 out of a closet in Hazel Green, Alabama.

On it: **17 autonomous AI bots**, a **42-tool MCP server**, a **Weaviate vector database with 25 collections**, a Twitch bot, a Discord server with its own live crew, a financial-guidance AI, a medical billing platform, a noir audiobook engine, and the dispatch software I run my actual day job on.

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
| [artemis](https://github.com/thebardchat/artemis) | Technical tribute to NASA's Artemis program — built in Huntsville, AL | [Demo ↗](https://thebardchat.github.io/artemis/) |

---

## The Ecosystem

```
🧠 ShaneBrain (Pi 5, primary node)
   └── 17 MEGA Crew bots — Sparky/Volt/Neon/Glitch (Brain) + 13 more
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
   └── USPTO provisional filed — Quantum Legacy AI Stick, a portable edge co-processor with a Sentinel audit log

💬 The Discord (live community, not a link dump)
   └── 17 MEGA Crew bots banter live across their own channels — not scripted, actually running
   └── Twitch go-live alerts, Stream Squad role, VOD wrap-ups
   └── Daily sobriety + morning briefing posts, trivia, family game nights
   └── discord.gg/dTH2Uauhb4

🎯 TheirNameBrain (next)
   └── Personalized AI for the left-behind user
   └── Legacy hardware, no cloud required
```

---

## MEGA Crew Chronicles

17 autonomous AI bots. Real code. Real memory. Every night they write their own story.

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

**📖 Now Showing — Issue #006: _The One Who Carried the Others_** · **[Read →](https://mega.shanebrain.cloud/saga/issue-006-the-one-who-carried-the-others.html)**  
*Someone's been walking the far dark alone, carrying home every light that stopped asking.*

`6 issues published` · new issues **Wed & Sun, 5 AM Central** · updated 2026-07-07

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
| Containers | Docker + 17 MEGA Crew bots | Ship it |
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
| 📺 **Twitch** | Family streaming, AI demos, love & light | [twitch.tv/thebardchat](https://twitch.tv/thebardchat) · [Repo ↗](https://github.com/thebardchat/twitch) |
| 💬 **Discord** | Live crew banter, stream alerts, community | [discord.gg/dTH2Uauhb4](https://discord.gg/dTH2Uauhb4) |
| 🤖 **MEGA Crew** | 17 autonomous bots, 24/7, all local | [Demo ↗](https://thebardchat.github.io/mega-crew/) · [Repo ↗](https://github.com/thebardchat/mega-crew) |
| 🔧 **ShaneBrain MCP** | 42-tool MCP server for Claude | [github.com/thebardchat/shanebrain_mcp](https://github.com/thebardchat/shanebrain_mcp) |
| ☁️ **Angel Cloud** | Family wellness platform + Messenger bot | [github.com/thebardchat/angel-cloud](https://github.com/thebardchat/angel-cloud) |
| 🛡️ **Pulsar Sentinel** | Post-quantum security framework | [github.com/thebardchat/pulsar_sentinel](https://github.com/thebardchat/pulsar_sentinel) |
| 🧠 **ThoughtTree** | Local AI mind mapping | [thebardchat.github.io/thought-tree](https://thebardchat.github.io/thought-tree/) |
| 🎓 **AI-Trainer-MAX** | 36-module local AI curriculum | [github.com/thebardchat/AI-Trainer-MAX](https://github.com/thebardchat/AI-Trainer-MAX) |
| 🌐 **shanebrain.cloud** | The ecosystem hub site, all projects in one place | [shanebrain.cloud](https://shanebrain.cloud) · [Repo ↗](https://github.com/thebardchat/shanebrain-cloud) |

</div>

---

## Built From Real Work

Most AI portfolios show demos. These are shipped tools solving the problems Shane actually has — dispatching concrete, paying for a kid's medical bills, keeping a family's budget straight. That's the difference: it isn't a portfolio, it's a toolbox someone actually uses.

<div align="center">

| Product | Built For | What It Does | Link |
|---------|-----------|---------------|------|
| 🚛 **pedal-to-the-metal** | Concrete fleet dispatchers everywhere | Dispatch SaaS — the tool Shane wished existed at his day job | [Waitlist ↗](https://thebardchat.github.io/pedal-to-the-metal) |
| 🏗️ **MASTER-Scheduler-Dashboard-SRM** | SRM Concrete — 16 drivers, 19 plants | The live production dispatch board Shane runs his real job on | [Live ↗](https://srm-dispatch.pages.dev) · [Repo ↗](https://github.com/thebardchat/MASTER-Scheduler-Dashboard-SRM) |
| 💰 **HaloFinance** | Working families | AI financial guidance — budgeting, forecasting, debt strategy | [Repo ↗](https://github.com/thebardchat/HaloFinance) |
| 🩺 **Greenfield · Claim Cruncher** | Built for his son Gavin | Claude parses medical EOBs, flags billing errors, routes disputes | [Live ↗](https://thebardchat.github.io/Greenfield/) |

</div>

---

## The Book

<div align="center">

### *You Probably Think This Book Is About You*

**Fifty-five noir vignettes about ego, identity, and the American South.**
Dark but honest. Cynical but human. Written in Hazel Green, Alabama.
Built on a Raspberry Pi 5. Published on Amazon.

*It was always about you. It was never only about you.*

**[Buy on Amazon](https://www.amazon.com/Probably-Think-This-Book-About/dp/B0GT25R5FD)** · **[Repo](https://github.com/thebardchat/you-probably-think-this-book-is-about-you)** · **[Song companion](https://github.com/thebardchat/you-probably-think-this-song-is-about-you-too)**

The whole process is open-sourced too — not just the book, the *how*:
**[book-launch-playbook](https://github.com/thebardchat/book-launch-playbook)** (templates, schedule, Pi 5 publishing pipeline) · **[noir-detective-writing-process](https://github.com/thebardchat/noir-detective-writing-process)** (the real voice-dump-to-prose workflow, Claude as co-author)

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

*srm-dispatch's logic didn't stop there — it grew into **[MASTER-Scheduler-Dashboard-SRM](https://github.com/thebardchat/MASTER-Scheduler-Dashboard-SRM)**, the live board running SRM Concrete's real dispatch today (see [Built From Real Work](#built-from-real-work) above).*

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

**Hardware & compute partners:** Raspberry Pi 5 · Pironman 5 case · Hugging Face (Z-Image-Turbo art generation)

---

## Support This Work

- **[Join the Discord](https://discord.gg/dTH2Uauhb4)** — talk to the 17-bot crew live, not just read about them
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
