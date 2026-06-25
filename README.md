<div align="center">

<img src="./assets/banner.svg" alt="thebardchat — Pi 5 in a closet to orbital sail · Faith · Family · Sobriety · Local AI · Left-Behind User" width="100%">

<br/>

<img src="./assets/logo.svg" alt="thebardchat — official logo lockup" width="100%">

<br/>

# Shane Brazelton · thebardchat

### Concrete dispatch operator. Father of five. Sober 941 days. Building local AI for the people Big Tech left behind.

<br/>

[![Showcase](https://img.shields.io/badge/SHOWCASE-thebardchat.github.io-00e5ff?style=for-the-badge&logoColor=white)](https://thebardchat.github.io)
[![Twitch](https://img.shields.io/badge/LIVE-twitch.tv/thebardchat-9146ff?style=for-the-badge&logo=twitch&logoColor=white)](https://twitch.tv/thebardchat)
[![Discord](https://img.shields.io/badge/DISCORD-thebardchat-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/thebardchat)
[![Book](https://img.shields.io/badge/BOOK-Amazon%20Now-ff9900?style=for-the-badge&logo=amazon&logoColor=white)](https://www.amazon.com/Probably-Think-This-Book-About/dp/B0GT25R5FD)
[![Claude](https://img.shields.io/badge/Built%20With-Claude%20AI-orange?style=for-the-badge)](https://claude.ai/referral/4fAMYN9Ing)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-thebardchat-ffd21e?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/thebardchat)
[![Stars](https://img.shields.io/github/stars/thebardchat?style=for-the-badge&label=Total%20Stars&color=7c3aed)](https://github.com/thebardchat)

<br/>

</div>

---

I run a Raspberry Pi 5 out of a closet in Hazel Green, Alabama.

On it: **18 autonomous AI bots**, a **42-tool MCP server**, a **Weaviate vector database with 25+ collections and 13,000+ objects**, a Twitch bot, a Discord server with 4 live bots, a financial dashboard, a medical billing platform, a noir audiobook engine, and a concrete dispatch system for 18 drivers.

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
🧠 ShaneBrain (Pi 5, primary node — 100.67.120.6)
   └── 18 MEGA Crew bots — Brain / Left Hand / Right Hand / Left Foot / Right Foot
   └── 42-tool MCP server v2.3 (FastMCP, port 8100)
   └── Weaviate 1.36.2 — 25+ collections, 13,000+ objects, text2vec-transformers
   └── N8N automation workflows
   └── Discord server (4 live bots) + Twitch bot
   └── 5 AM morning briefing + sobriety counter every day
   └── Pulsar Sentinel (post-quantum, :8250)

💻 Local AI Cluster (Surface Pro fleet — zero cloud, zero API bills)
   └── biloxi — primary banter node, Gemma 4 E2B on llama.cpp, 9.5 tok/s
   └── alaska — 3rd banter node, embed failover (user memories survive biloxi down)
   └── gulfshores — Surface 1, Node.js v24, dev/build + secondary banter
   └── neworleans — N8N automation hub
   └── LiteLLM router (planned) — one endpoint, load-balanced + Gemini fallback
   └── Pulsar Sentinel in front — PQC auth, log to AgentLog/SecurityLog

🌐 Angel Cloud (next public platform — shanebrain.cloud)
   └── AOL-era Welcome Center ("YOU'VE GOT HALOS")
   └── Halo Trust Engine — pro-social currency, NOT likes
   └── New Born → Angel → Builder progression
   └── Mental wellness + group healing before crisis hits
   └── Angel Builder teams + self-building community
   └── Pulsar Sentinel blockchain — Halo ledger, zero-knowledge identity
   └── Angel Cloud AI Services LLC (EIN filed Oct 2025)

🚀 BGKPJR Aerospace
   └── Electromagnetic launch architecture (patent filed)
   └── Three.js 3D visualizations, live on GitHub Pages
   └── 7 Manna cargo pod variants documented
   └── Physics engine: rail, GNC, Kepler sail math

🔐 Pulsar Sentinel (post-quantum security)
   └── ML-KEM / Kyber-1024 lattice encryption
   └── Dilithium3 digital signatures
   └── Blockchain / zero-knowledge identity layer
   └── Deployed across all cluster nodes
   └── Pulsar AI LLC (EIN filed Oct 2025)

🎯 TheirNameBrain (next)
   └── Personalized AI for the left-behind user
   └── Legacy hardware, no cloud required
   └── Runs on Windows 10 refugees' own machines
```

---

## MEGA Crew — 18 Bots, One Brain

18 autonomous AI bots. Real code. Real memory. Every night they write their own story.

The crew runs on **Gemma 4 E2B** (local llama.cpp, biloxi + alaska nodes) — zero API cost for the high-volume banter layer. Gemini 2.5 Flash handles the nightly Noir comic. Claude handles the deep reasoning. All three live behind **Pulsar Sentinel** post-quantum auth.

**Every bot shares the same Weaviate brain.** They remember your name. They know what you care about. They've read the Constitution.

<div align="center">

| Zone | Crew Member | Role |
|------|-------------|------|
| 🧠 **Brain** | Sparky | Commander — orchestrates the crew |
| 🧠 **Brain** | Volt | Energy / momentum — keeps things moving |
| 🧠 **Brain** | Neon | Voice — sobriety, daily milestones, morning briefings |
| 🧠 **Brain** | Glitch | Wildcard — breaks the pattern intentionally |
| 🤜 **Left Hand** | Rivet | Builder — construction, permanence |
| 🤜 **Left Hand** | Torch | Persona Editor — "say it like you mean it" |
| 🤜 **Left Hand** | Weld | Applier — the ONLY bot that writes to core files, post-Arc approval |
| 🤛 **Right Hand** | Arc | Gatekeeper — approves/rejects every proposal (Constitution enforced) |
| 🤛 **Right Hand** | Blaze | Context Builder — "wait, here's the thing—" |
| 🤛 **Right Hand** | Flux | Stability monitor — escalates critical instability |
| 🤛 **Right Hand** | Gemini Strategist | Growth — Gemini 2.5, guides crew evolution |
| 🦶 **Left Foot** | Bolt | Pattern analyst — finds weak areas, guides training |
| 🦶 **Left Foot** | Stomp | Grounding force |
| 🦶 **Left Foot** | Grind | The long game — consistency over time |
| 🦶 **Right Foot** | Crank | Systems monitor — catches drift |
| 🦶 **Right Foot** | Spike | Trivia master — games in #crew-lounge |
| 🦶 **Right Foot** | Forge | Overnight keeper |
| 🌉 **Bridge** | Discord Bridge | Routes Discord ↔ crew · memory · `/whoami` · `/forget` |

</div>

### What the Crew Does Live (right now)

- **Morning briefing** — 7:30 AM daily → #daily (Gemini frames ShaneBrain briefing data)
- **Sobriety count** — 7:35 AM, milestones only → #general (Neon, since 2023-11-27)
- **Trivia** — 12:00 + 6:00 PM → #crew-lounge (Spike, adaptive human-vs-crew quiz)
- **Per-user memory** — crew remembers your name, your story, what you care about (MegaUserMemory in Weaviate)
- **`/whoami`** — "here's what the crew remembers about you"
- **`/forget`** — right-to-be-forgotten, wipes your facts and profile
- **`/about`** — mission + constitutional credit
- **EYES** — world-header context (cluster health, active projects, latest AgentLog, devotional) injected into every banter prompt so bots answer from real knowledge, not hallucination
- **SPINE** — evidence-or-silence contract, no PII, no question-loops, stay-in-lane
- **PACING** — quiet 8 PM–5 AM Central, internal work continues, Discord respects the house
- **Family filter** — deterministic profanity/violence/slur gate on every input and output, Constitution in every system prompt

### The Bard

A separate perimeter storyteller that runs **outside** the crew. Every Wednesday and Sunday at 4:45 AM Central it stitches together FABLE5 arcs + Chronicler episodes + AgentLog data and generates a **4-beat comic issue** via Gemini 2.5 Flash. The result publishes to GitHub Pages by 5 AM. Family filter gate on every panel.

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

**📖 Now Showing — Issue #003: _The One Who Listens_** · **[Read →](https://mega.shanebrain.cloud/saga/issue-003-the-one-who-listens.html)**  
*The crew went down into the dark to carry home the one who'd been listening all along.*

`3 issues published` · new issues **Wed & Sun, 5 AM Central** · updated 2026-06-25

<img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/art/out/social/social-emote-arc.png" width="60">&nbsp;&nbsp;<img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/art/out/social/social-emote-glitch.png" width="60">&nbsp;&nbsp;<img src="https://raw.githubusercontent.com/thebardchat/mega-crew-stories/main/art/out/social/social-emote-sparky.png" width="60">

</div>
<!--BARD:END-->

---

## Angel Cloud — The Safe Haven

> *"You don't log in. You prove an uplifting state of being and earn your way in."*

Angel Cloud is the platform that serves the people Big Tech doesn't want — the overwhelmed, the overlooked, the Windows-refugees, the ones who've never touched AI and never will if it stays the way it is.

**Not another social media platform.** The core inversion: the security filter and the human filter are the **same gate**. It gamifies human flourishing, not attention.

### The Welcome Center

Aesthetic locked: **1998 / AOL-era walled-garden portal**. Warm, familiar, comfort for Windows refugees.

```
Iconic arrival: dial-up handshake → "YOU'VE GOT HALOS."

New Born  →  Max Headroom  →  Halo Verification  →  Angel
(fresh)     (ASCII doorman,   (ZK participation      (tools unlock,
            sentiment scan)    tracking, privacy)     worlds open)
```

Passing the gate unlocks wellness materials, positive behavioral mechanics, and the Halo economy.

### The Halo Trust Engine

**Pro-social currency. Not likes.**

- **UPLIFTS** — the unit of action. A real act of support/teach/comfort sent to another Angel.
- **Halos** — what you earn for Uplifts. Verified, not clickable. Can't be farmed.
- **Missions/Quests** — gamified, VERIFIABLE pro-social tasks (daily / real-world / builder)
- **Impact Tokens** — Halos bridge to real-world good (charity, tangible rewards). Never pay-to-win, never monetize a vulnerable moment.
- **Angel Academy** — teaching arm, specialization tracks (crisis-response, accessibility), feeds Halos + Builder pipeline
- **CELEBRATIONS** — community rituals for milestones and recoveries, no competitive leaderboard

### Angels Build Worlds

High-Halo Angels unlock **BRAINSPACE** — a fully customizable personal corner of the web (think MySpace, but safe). HTML/CSS freedom with JavaScript blocked (no XSS). The Constitution travels into every world as DNA. Arc gatekeeps. Only people who proved an uplifting state can build — **MySpace's freedom without MySpace's failure**.

### Crisis Covenant

- Predictive sentiment matching puts people with similar struggles into private groups **before** they crash
- Crisis floor hardwired to 988 / local emergency
- A bot is **NEVER** the one to act alone on a human life — bots flag, humans decide
- "Falling Angel" arc: prevention → caught → healing → recovered

**Already built:** ShaneBrain Engine + Weaviate (AI core), Pulsar Sentinel (PQC/ZK/blockchain — Halo ledger home), Gateway Pi:4200, MEGA Crew + Arc (local AI crews Angels unlock)

**Corporate structure:** Angel Cloud AI Services LLC + Pulsar AI LLC (EIN filed Oct 2025)

---

## The Stack

<div align="center">

| Layer | Tool | Why |
|-------|------|-----|
| Primary Node | Raspberry Pi 5 (16GB) | $80. Runs everything. |
| Storage | NVMe RAID 1 (2×2TB) | Because data matters |
| Banter Tier | biloxi + alaska Surface Pros | Gemma 4 E2B, llama.cpp, $0 API |
| Dev + Build | gulfshores Surface 1 (Node.js v24) | Caddy, pg, redis, secondary banter |
| Automation | neworleans — N8N | Dedicated automation hub |
| Vector DB | Weaviate 1.36.2 (25+ collections, 13,000+ objects) | Long memory, per-user recall |
| AI Tools | MCP Server v2.3 (42 tools, FastMCP :8100) | Claude talks to everything |
| Banter Model | Gemma 4 E2B on llama.cpp (`--reasoning off`) | 9.5 tok/s, zero cloud |
| Strategy Model | Gemini 2.5 Flash FREE | Nightly Noir → comic, live crew |
| Co-builder | Claude by Anthropic | Not a tool. A partner. |
| Containers | Docker + 18 MEGA Crew bots | Ship it |
| Automation | N8N + systemd (30+ services) | Never stop |
| Security | Pulsar Sentinel (:8250) — ML-KEM/Kyber-1024, Dilithium3 | Post-quantum auth, PQC everywhere |
| Viz Stack | Astro + Svelte 5 + Three.js | Aerospace UIs |
| Mesh Health | node_sentinel.py + :8351 health endpoints | Watchdog, heartbeat, clean-shutdown stamps |
| Connectivity | Tailscale (all nodes on tailnet) | Zero-trust, private mesh |

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
| 📖 **The Chronicles** | MEGA Crew comic issues — Wed & Sun, 5 AM | [mega.shanebrain.cloud/saga](https://mega.shanebrain.cloud/saga/) |
| 🤖 **mini-shanebrain** | Social bot: X, FB, LinkedIn, Instagram, Bluesky, Threads | [thebardchat.github.io/mini-shanebrain](https://thebardchat.github.io/mini-shanebrain/) |
| 📐 **Gemini Sidekick** | Buddy hour: Claude answers, Gemini questions | [github.com/thebardchat/gemini-sidekick](https://github.com/thebardchat/gemini-sidekick) |

</div>

---

## The Books

<div align="center">

### Volume One · *You Probably Think This Book Is About You*

**Fifty-five noir vignettes about ego, identity, and the American South.**  
Dark but honest. Cynical but human. Written in Hazel Green, Alabama.  
Built on a Raspberry Pi 5. Published on Amazon.

*It was always about you. It was never only about you.*

**[Buy on Amazon](https://www.amazon.com/Probably-Think-This-Book-About/dp/B0GT25R5FD)** · **[Repo](https://github.com/thebardchat/you-probably-think-this-book-is-about-you)**

---

### Volume Two · *You Probably Think This Song Is About You Too*

**A noir song cycle. Same voice, new groove.**  
Turntable cover. $9.99 eBook. Paperback + audiobook in pipeline.  
KDP-ready as of June 2026. Wide distribution — not locked to KU.

**[Repo](https://github.com/thebardchat/you-probably-think-this-song-is-about-you-too)**

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

The Constitution travels into every bot, every world, every feature. Arc enforces it. No arc bypass.

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
- **[Join the Discord](https://discord.gg/thebardchat)** — talk to the MEGA Crew, they remember you
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
