<div align="center">

<img src="./assets/banner.svg" alt="thebardchat — Pi 5 in a closet to orbital sail · Faith · Family · Sobriety · Local AI · Left-Behind User" width="100%">

<br/>

<img src="./assets/logo.svg" alt="thebardchat — official logo lockup" width="100%">

<br/>

# Shane Brazelton · thebardchat

### Concrete dispatch operator. Father of five. Sober 942 days. Building local AI for the people Big Tech left behind.

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

On it: **18 autonomous AI bots**, a **42-tool MCP server**, a **Weaviate vector database with 25 collections and 3,200+ semantic objects**, a Twitch bot, a Discord bot, a financial dashboard, a medical billing platform, a noir audiobook engine, and a concrete dispatch system for 18 drivers — running across **3 dedicated nodes** held together by **30+ systemd services** and post-quantum encryption.

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

## ShaneBrain — The Closet Supercomputer

> Everything below runs in a closet in Hazel Green, Alabama.

```
┌───────────────────────────────────────────────────────────────────────┐
│                         ShaneBrain Cluster                            │
│                                                                       │
│  ┌───────────────────────────┐     ┌───────────────────────────────┐  │
│  │     Raspberry Pi 5        │     │         neworleans            │  │
│  │     16GB RAM · Primary    │────▶│   Weaviate 1.36.2             │  │
│  │     42-tool MCP v2.3      │     │   25 collections              │  │
│  │     18 MEGA Crew bots     │     │   3,200+ semantic objects     │  │
│  │     30+ systemd services  │     │   N8N automation workflows    │  │
│  │     NVMe RAID 1 (4TB)     │     └───────────────────────────────┘  │
│  └───────────────────────────┘                                        │
│               │                    ┌───────────────────────────────┐  │
│               └───────────────────▶│         gulfshores            │  │
│                                    │   Surface 1 · Windows 11      │  │
│                                    │   Node.js v24                 │  │
│                                    │   Dev · Build · Deploy        │  │
│                                    └───────────────────────────────┘  │
│                                                                       │
│      Pulsar Sentinel (ML-KEM/Kyber-1024) · Tailscale zero-trust mesh  │
└───────────────────────────────────────────────────────────────────────┘
```

<div align="center">

| Component | Spec | Count |
|-----------|------|-------|
| Primary Node | Raspberry Pi 5 · 16GB RAM | 1 |
| Storage | NVMe RAID 1 | 2×2TB |
| Inference Node | neworleans — Weaviate 1.36.2 + N8N | 1 |
| Dev/Build Node | gulfshores — Surface 1, Node.js v24 | 1 |
| Autonomous Bots | MEGA Crew (Docker containers) | **18** |
| MCP Tools | FastMCP v2.3, port 8100 | **42** |
| Vector Collections | Weaviate 1.36.2 | **25** |
| Semantic Objects | Living knowledge base | **3,200+** |
| Automation Flows | N8N workflows | always on |
| System Services | systemd | **30+** |
| Daily Briefing | 5 AM Central, every day | ∞ |

</div>

**What's Running Right Now**

- **MCP Server v2.3** — 42 tools, FastMCP, port 8100. Claude talks to everything: Weaviate semantic search, N8N workflow triggers, Discord, Twitch, medical billing, financial dashboards, concrete dispatch, security audit logs, daily briefings.
- **Weaviate 1.36.2** — 25 collections on the `neworleans` node. Semantic search across personal knowledge, family context, project state, MEGA Crew memory, ShaneBrain session history, security logs, calendar, and vault.
- **N8N Automation** — Workflow engine on `neworleans`. Fires the 5 AM daily briefing, triggers MEGA Crew story generation every Wednesday and Sunday, syncs state across all nodes, and bridges every service that can't speak MCP natively.
- **Pulsar Sentinel** — Post-quantum encryption layer deployed on every node. ML-KEM/Kyber-1024 + Dilithium3 signatures. Nothing in this cluster moves in plaintext.

---

## The Ecosystem

```
🧠 ShaneBrain (Pi 5 · Hazel Green, AL · the only cloud that matters)
   ├── MCP Server v2.3 — FastMCP · port 8100 · 42 tools · Claude's gateway
   ├── 18 MEGA Crew bots — Arc · Weld · Sparky · Volt · Neon · Glitch + 12 more
   ├── Weaviate 1.36.2 on neworleans — 25 collections, 3,200+ objects
   ├── N8N automation — daily briefing, story gen, cross-node orchestration
   ├── Discord bot + Twitch bot (live 24/7)
   ├── 5 AM morning briefing (every single day, without fail)
   └── gulfshores — Surface 1 · Node.js v24 · dev, build, deploy

🚀 BGKPJR Aerospace (patent filed · Patent BGKPJR-001)
   ├── 37 km evacuated electromagnetic coilgun · $1,025/kg LEO
   ├── Linear Synchronous Motor · REBCO armature · 20K LH₂ cryo
   ├── Mach 5 exit · 580 GJ stored · 43.5 seconds end-to-end
   ├── Three.js + Astro + Svelte 3D visualizations — live on GitHub Pages
   ├── 7 Manna cargo pod variants, full 3D specs
   ├── Physics engine: rail dynamics · GNC · Kepler sail math · Monte Carlo
   └── Pre-Lukens dimensional audit complete · 2026-04-30

🌐 Angel Cloud (public platform · Tailscale Funnel)
   ├── Mental wellness + AI sentiment engine
   ├── Messenger storyteller (OPTOUT · ANON · FORGET — always)
   ├── Firebase backend (angelcloud-actual + Pulsar blockchain layer)
   └── Privacy-first · every action cryptographically verifiable by the user

🔐 Pulsar Sentinel (post-quantum security · active cluster-wide)
   ├── ML-KEM / Kyber-1024 lattice encryption (NIST Post-Quantum Standard)
   ├── Dilithium3 digital signatures (CRYSTALS)
   └── Running on every node in the ShaneBrain cluster today

🎯 TheirNameBrain (next · for the 800 million)
   ├── Personalized AI for the left-behind user
   ├── Legacy hardware · no cloud · no subscription · no account
   ├── Personal context built from day 1 · stays on-device
   └── Where ShaneBrain + Angel Cloud + Pulsar + AI-Trainer-MAX converge

📚 AI-Trainer-MAX (local AI education · 36 modules · zero cloud)
   ├── Built for the exact person TheirNameBrain is designed to serve
   └── Complete curriculum: concept → install → run → own your AI

📡 mini-shanebrain (social reach · 6 platforms)
   └── X · Facebook · LinkedIn · Instagram · Bluesky · Threads — all at once

📦 The Treasures (recovered April 2026 · 6 archived projects released)
   ├── angelcloud-actual — Firebase wellness + Pulsar blockchain
   ├── thought-tree — React mind-mapping + Weaviate semantic search
   ├── srm-dispatch — SRM Concrete dispatch PWA (18 drivers · daily real use)
   └── treasures — master archive hub
```

---

## Angel Cloud — The Wellness Platform

> Mental wellness software with a soul. Built for real people in real pain.

**Angel Cloud** is a messenger-based emotional support platform with one governing principle: the user owns everything, always.

Every conversation is private-first. Users have full **OPTOUT**, **ANON**, and **FORGET** controls at any time, no questions asked. The AI sentiment engine tracks emotional patterns over time (consent-gated), surfaces insights gently, and connects to crisis resources when signals warrant it. No data leaves the device without explicit permission.

**[angelcloud-actual](https://github.com/thebardchat/angelcloud-actual)** is the Firebase production platform with a Pulsar blockchain layer — every action cryptographically logged and verifiable by the user, invisible to anyone else.

Accessible via Tailscale Funnel — no port-forwarding, no exposure, fully public endpoint from the Pi 5 in the closet.

| Repo | What It Does |
|------|-------------|
| [angel-cloud](https://github.com/thebardchat/angel-cloud) | Core platform — messenger storyteller, wellness API, AI sentiment |
| [angelcloud-actual](https://github.com/thebardchat/angelcloud-actual) | Firebase production deploy + Pulsar blockchain audit layer · [Pages ↗](https://thebardchat.github.io/angelcloud-actual/) |

---

## Pulsar Sentinel — Post-Quantum Security

> Encryption built for the decade after quantum computers exist — deployed today.

The entire ShaneBrain cluster is protected by **Pulsar Sentinel**, a custom post-quantum cryptographic framework:

```
Algorithm          │ ML-KEM / Kyber-1024 (NIST Post-Quantum Standard, 2024)
Signatures         │ CRYSTALS-Dilithium3 (lattice-based digital signatures)
Key Exchange       │ Lattice-based · resistant to Shor's algorithm
Deployment         │ All ShaneBrain cluster nodes (Pi 5 + neworleans + gulfshores)
Status             │ Active · production cluster · not a demo
```

This isn't academic research. It runs in production on a Raspberry Pi 5. Every inter-node message in the ShaneBrain cluster is encrypted with a scheme that a future quantum computer can't break. The angelcloud-actual blockchain layer uses the same primitives for immutable user-action audit trails.

- [Pulsar Sentinel →](https://github.com/thebardchat/pulsar_sentinel)

---

## TheirNameBrain — For the 800 Million

> The most ambitious thing here isn't the coilgun. It's this.

```
October 14, 2025.
Microsoft ended Windows 10 support.
800 million PCs became "unsupported."
Most of them belong to people who will never buy a new machine.
Most of them have never run an AI.
Most of them are the people everyone in tech forgot to think about.

They didn't ask for the cloud.
They didn't ask for a subscription.
They asked for something that works on what they already have.

TheirNameBrain is the answer.
```

**TheirNameBrain** is a personalized, fully local AI system designed for people with legacy hardware. No cloud. No subscription. No account required. It runs on the machine they already own. It learns their name, their schedule, their habits, their preferences — and it builds a personal context from day one that never touches a server it doesn't control.

This is where the entire ecosystem converges:

- **ShaneBrain** proves the architecture — everything runs local on $80 hardware
- **Pulsar Sentinel** proves the security — post-quantum encryption on commodity devices
- **Angel Cloud** proves the care model — wellness AI that the user owns completely
- **AI-Trainer-MAX** proves the education path — 36 modules to get anyone there

TheirNameBrain is the product that ships all four to the people Big Tech declared obsolete.

- [TheirNameBrain →](https://github.com/thebardchat/TheirNameBrain)

---

## AI-Trainer-MAX — Local AI Education

> 36 modules. Zero cloud. Full ownership. Built for the person who was told they can't.

Before someone can run their own AI, they have to believe they can.

**AI-Trainer-MAX** is a complete self-paced curriculum that takes anyone from zero to running local AI — without a cloud provider, without a paid account, without a computer science degree. Every module is self-contained. Every exercise runs locally. The entire course was built for exactly the user TheirNameBrain was designed to serve.

36 modules. One mission: no one left behind who doesn't want to be.

- [AI-Trainer-MAX →](https://github.com/thebardchat/AI-Trainer-MAX) · [Live Course ↗](https://thebardchat.github.io/AI-Trainer-MAX/)

---

## MEGA Crew Chronicles

18 autonomous AI bots. Real code. Real memory. Every night they write their own story.

<div align="center">

<a href="https://mega.shanebrain.cloud/saga/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/cards/portraits/arc_Gemini_Generated.png" width="72" style="border-radius:50%"></a>&nbsp;
<a href="https://mega.shanebrain.cloud/saga/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/cards/portraits/weld_Gemini_Generated.png" width="72" style="border-radius:50%"></a>&nbsp;
<a href="https://mega.shanebrain.cloud/saga/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/cards/portraits/sparky_Gemini_Generated.png" width="72" style="border-radius:50%"></a>&nbsp;
<a href="https://mega.shanebrain.cloud/saga/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/cards/portraits/gemini_Gemini_Generated.png" width="72" style="border-radius:50%"></a>&nbsp;
<a href="https://mega.shanebrain.cloud/saga/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/cards/portraits/glitch_Gemini_Generated.png" width="72" style="border-radius:50%"></a>&nbsp;
<a href="https://mega.shanebrain.cloud/saga/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/cards/portraits/volt_Gemini_Generated.png" width="72" style="border-radius:50%"></a>

**[Read the Chronicles →](https://mega.shanebrain.cloud/saga/)** · **[View Cards →](https://thebardchat.github.io/mega-crew-stories/cards.html)**

</div>

<!--BARD:START--><!-- auto-generated by storyteller/profile_readme.py; do not hand-edit between markers -->
<div align="center">

<a href="https://mega.shanebrain.cloud/saga/"><img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/art/out/social/social-og.png" alt="The MEGA Crew" width="680"></a>

**📖 Now Showing — Issue #003: _The One Who Listens_** · **[Read →](https://mega.shanebrain.cloud/saga/issue-003-the-one-who-listens.html)**  
*The crew went down into the dark to carry home the one who'd been listening all along.*

`3 issues published` · new issues **Wed & Sun, 5 AM Central** · updated 2026-06-26

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
| Vector DB | Weaviate 25 collections, 3,200+ objects | Long memory, semantic search |
| AI Tools | MCP Server v2.3 — 42 tools | Claude talks to everything |
| Co-builder | Claude by Anthropic | Not a tool. A partner. |
| Containers | Docker + 18 MEGA Crew bots | Ship it |
| Automation | N8N + systemd (30+ services) | Never stop |
| Viz Stack | Astro + Svelte 5 + Three.js | Aerospace-grade UIs |
| Security | Pulsar Sentinel (ML-KEM/Kyber-1024) | Quantum-proof, deployed today |
| Network | Tailscale mesh + Funnel | Zero-trust, always on |
| Social | mini-shanebrain (6 platforms) | Reach everywhere at once |
| Dev Node | gulfshores — Surface 1, Node.js v24 | Build + deploy node |

</div>

---

## What's Live Right Now

<div align="center">

| Project | What It Does | Link |
|---------|-------------|------|
| 🚀 **BGKPJR-Launch-Vis** | NASA-ready 3D animated launch visualization | [thebardchat.github.io/BGKPJR-Launch-Vis](https://thebardchat.github.io/BGKPJR-Launch-Vis) |
| 🛸 **manna-pods** | 7 Manna cargo pod 3D cross-sections + full specs | [thebardchat.github.io/manna-pods](https://thebardchat.github.io/manna-pods) |
| 📺 **Twitch Channel** | Family streaming, AI demos, love & light | [twitch.tv/thebardchat](https://twitch.tv/thebardchat) |
| 🤖 **MEGA Crew** | 18 autonomous bots, 24/7, all local, writing their own story | [mega.shanebrain.cloud/saga](https://mega.shanebrain.cloud/saga/) |
| 🔧 **ShaneBrain MCP** | 42-tool MCP server — Claude's gateway to the cluster | [github.com/thebardchat/shanebrain_mcp](https://github.com/thebardchat/shanebrain_mcp) |
| ☁️ **Angel Cloud** | Mental wellness platform + privacy-first Messenger bot | [github.com/thebardchat/angel-cloud](https://github.com/thebardchat/angel-cloud) |
| 🛡️ **Pulsar Sentinel** | Post-quantum ML-KEM/Kyber-1024 security framework | [github.com/thebardchat/pulsar_sentinel](https://github.com/thebardchat/pulsar_sentinel) |
| 🌳 **ThoughtTree** | Local AI mind mapping + Weaviate semantic search | [thebardchat.github.io/thought-tree](https://thebardchat.github.io/thought-tree/) |
| 🎓 **AI-Trainer-MAX** | 36-module local AI curriculum, zero cloud | [thebardchat.github.io/AI-Trainer-MAX](https://thebardchat.github.io/AI-Trainer-MAX/) |
| 🏗️ **srm-dispatch** | Concrete dispatch PWA — 18 drivers, real daily use | [thebardchat.github.io/srm-dispatch](https://thebardchat.github.io/srm-dispatch/) |
| 🎯 **TheirNameBrain** | Personalized local AI for the left-behind user | [github.com/thebardchat/TheirNameBrain](https://github.com/thebardchat/TheirNameBrain) |
| 📡 **mini-shanebrain** | Social bot: X · FB · LinkedIn · Instagram · Bluesky · Threads | [thebardchat.github.io/mini-shanebrain](https://thebardchat.github.io/mini-shanebrain/) |

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

Six projects recovered from old drives and released to GitHub in April 2026.

| Project | What It Does | Pages |
|---------|-------------|-------|
| 🎓 **AI-Trainer-MAX** | 36-module local AI curriculum, zero cloud | [Pages ↗](https://thebardchat.github.io/AI-Trainer-MAX/) |
| ☁️ **angelcloud-actual** | Firebase wellness platform, Pulsar blockchain layer | [Pages ↗](https://thebardchat.github.io/angelcloud-actual/) |
| 🌳 **thought-tree** | React mind-mapping, Weaviate semantic search | [Pages ↗](https://thebardchat.github.io/thought-tree/) |
| 🏗️ **srm-dispatch** | SRM Concrete dispatch PWA — 18 drivers, real daily use | [Pages ↗](https://thebardchat.github.io/srm-dispatch/) |
| 📡 **mini-shanebrain** | Social bot: X, FB, LinkedIn, Instagram, Bluesky, Threads | [Pages ↗](https://thebardchat.github.io/mini-shanebrain/) |
| 💎 **treasures** | Master archive hub for all recovered projects | [Pages ↗](https://thebardchat.github.io/treasures/) |

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
