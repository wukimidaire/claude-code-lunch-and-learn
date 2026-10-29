# 01 — Metaskills: turn a repeated workflow into a skill (20 min)

## Prerequisites

- [ ] [00 Setup](00-setup.md) done
- [ ] One task you do **every week** with Claude or by hand (a report, a client email, a meeting prep, a data clean-up…)

## What you will build

A reusable skill in `.claude/skills/<your-skill>/SKILL.md` — diagnosed, designed, written *with* Claude, tested and audited.
**Metaskills** are skills that build skills: you use them to scale yourself.

## The 6 metaskills: one chain

```
/problem-statement  →  /problem-solution  →  /compare-options  →  /interview  →  /skill-creator  →  /skill-audit
   diagnose              solve                  decide                specify        build               check
```

| Metaskill | Question it answers |
|---|---|
| `/problem-statement` | What's the *real* problem? (diagnosis only, no solutions) |
| `/problem-solution` | What does "solved" look like, what depends on what, and in what order do we build it? |
| `/compare-options` | Which option wins, with pros and cons? |
| `/interview` | What exactly do I want? (inputs, outputs, edge cases, what "good" looks like) |
| `/skill-creator` | Turn all of that into a working `SKILL.md` |
| `/skill-audit` | Is the skill well-built? What should be fixed first? |

## Steps

| Min | Step | What to type |
|---|---|---|
| 0–3 | **Diagnose** | `/problem-statement I spend too much time on <your workflow>`. Confirm or correct the problem it distills. |
| 3–6 | **Solve** | `/problem-solution`. It maps the desired end state, the dependencies (data, tools, people) and the build order. |
| 6–8 | **Decide** | `/compare-options` with *a skill vs a script vs keep doing it manually*. Pick the winner. (If it's not "skill", choose another workflow.) |
| 8–11 | **Specify** | `/interview`. Answer honestly; Claude digs for inputs, outputs, edge cases and what "good" looks like. |
| 11–15 | **Build** | `/skill-creator`. It turns everything above into `.claude/skills/<name>/SKILL.md`. |
| 15–18 | **Test** | Start a fresh conversation (`/clear`), then trigger your skill with a real example. |
| 18–20 | **Check** | `/skill-audit <name>`. Fix the top finding. |

> **Running late?** `/skill-creator` calls `/interview`, `/problem-statement` and `/problem-solution` itself,
> so you can jump straight to it and still get a skill. The explicit chain above teaches you what each step does.

## Verification

- [ ] You used all 6 metaskills at least once
- [ ] `.claude/skills/<name>/SKILL.md` exists with a `name` and `description`
- [ ] Your skill shows up when you type `/`
- [ ] It produced a useful result on a real example in a fresh conversation

## Why this matters

A prompt helps once. A skill is **captured know-how** that runs every time, for you and your team.
The chain itself is systems thinking: **deconstruct** (problem-statement), **analyse** (problem-solution, interview), **decide** (compare-options), **test** (test and audit).
That's the first building block of your company's digital twin.

## Take-home

- Run the chain on your top-3 weekly tasks
- Use `/problem-statement` → `/problem-solution` → `/compare-options` on any decision, not just skills
- Move good skills to `~/.claude/skills/` so they work in every project

➡️ Next: [02 Book-to-skill](02-book-to-skill.md)
