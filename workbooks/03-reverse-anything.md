# 03 — Reverse anything: rebuild a feature from scratch (20 min)

## Prerequisites

- [ ] Node.js 22+ and the **rea** plugin connected (`/mcp` shows `rea`) — see [00 Setup](00-setup.md)
- [ ] A target you are **allowed** to inspect:
  - a public website (a pricing calculator, a search box, an onboarding flow…)
  - an app you own or licensed on your machine (Electron apps such as VSCode, Obsidian, Notion desktop…)
  - your own company's tool

> ⚖️ **Rules of the game.** Learn *how* something works, then build *your own* version.
> Don't bypass logins, paywalls, DRM or licence checks. Don't copy or redistribute proprietary code.
> Respect the target's terms of service.

## What you will build

A minimal, working version of one feature you admire — built **from scratch** in `builds/<name>/`,
plus a skill that captures the pattern so you can do it again.

## Steps

| Min | Step | What to type |
|---|---|---|
| 0–3 | **Pick one feature** | `/problem-statement I want to understand how <feature> in <target> works and build my own version` |
| 3–10 | **Reverse it with evidence** | "Use rea to analyse how `<feature>` works in `<target>`. Show me the evidence (files, requests, functions) and the limitations." |
| 10–12 | **Capture the pattern** | `/skill-creator` — "make a skill that explains this pattern and how to build it" |
| 12–19 | **Build it from scratch** | "Using what we learned, build a minimal working version in `builds/<name>/`. Plain HTML/JS or Python. Tell me how to run it." |
| 18–19 | **Run it** | Open it / run it. Show your neighbour. |
| 19–20 | **Open the closing presentation** | In the terminal: `python3 scripts/open_presentation.py` (Windows: `python scripts\open_presentation.py`). Or ask Claude: *"run scripts/open_presentation.py"* |

### Prompt ideas

- "Understand how the search in `<app>` ranks results, show me the evidence, and build a similar search for a CSV of my products."
- "How does `<website>`'s pricing calculator compute its price? Rebuild it as a single HTML page with my own pricing."
- "How does `<Electron app>` store its settings and sync state? Build a tiny app that does the same for my notes."

## No-rea fallback

If rea won't install: pick a **public website**, open the browser devtools (Network + Sources tabs),
copy what you observe (requests, HTML structure) into Claude, and do the same steps.

## Verification

- [ ] `builds/<name>/` contains a working build you wrote with Claude (not copied code)
- [ ] You can explain how the original feature works, with evidence
- [ ] A new skill captures the pattern

## Why this matters

Every product is a system of **parts → connections → patterns**. Reverse engineering makes the hidden parts
visible — the core move of systems thinking. Then Claude Code turns understanding into something you own.

## Take-home

- rea: <https://github.com/morluto/rea> — `rea update` keeps it current
- Do this on one internal tool your team pays for but only uses 10% of

➡️ Next: the systems-thinking presentation. Open it with

```bash
python3 scripts/open_presentation.py
```

(or open [the slides](../presentation/system-thinking/index.html) directly)
