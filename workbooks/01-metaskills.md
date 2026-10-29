# 01 — Metaskills: turn a repeated workflow into a skill (15 min)

## Prerequisites

- [ ] [00 Setup](00-setup.md) done
- [ ] One task you do **every week** with Claude or by hand (a report, a client email, a meeting prep, a data clean-up…)

## What you will build

A reusable skill in `.claude/skills/<your-skill>/SKILL.md` — written *with* Claude, tested, and audited.
**Metaskills** are skills that build skills: you use them to scale yourself.

## Steps

| Min | Step | What to type |
|---|---|---|
| 0–3 | **Find the real problem** | `/problem-statement I spend too much time on <your workflow>` — confirm or correct the problem it distills |
| 3–8 | **Get interviewed** | `/interview` — answer honestly. Claude digs for inputs, outputs, edge cases, what "good" looks like |
| 8–12 | **Create the skill** | `/skill-creator` — it turns the interview into `.claude/skills/<name>/SKILL.md` |
| 12–14 | **Test it** | Start a fresh conversation (`/clear`), then trigger your skill with a real example |
| 14–15 | **Audit it** | `/skill-audit <name>` — fix the top finding |

## Verification

- [ ] `.claude/skills/<name>/SKILL.md` exists with a `name` and `description`
- [ ] Your skill shows up when you type `/`
- [ ] It produced a useful result on a real example in a fresh conversation

## Why this matters

A prompt helps once. A skill is **captured know-how** that runs every time, for you and your team.
That's the first building block of your company's digital twin.

## Take-home

- Turn your top-3 weekly tasks into skills
- Move good skills to `~/.claude/skills/` so they work in every project

➡️ Next: [02 Book-to-skill](02-book-to-skill.md)
