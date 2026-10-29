# Claude Code Advanced — Lunch & Learn

> From prompts to systems: build skills, turn books into expertise, reverse-engineer anything —
> and see why Claude Code is the gateway to your company's digital twin.

**Wintercircus · 12:00 – 14:00**

## Schedule

| Time | Block | Material |
|---|---|---|
| 12:00 – 12:20 | Keynote — context (live only) | — |
| 12:20 – 12:30 | Setup — install, clone, trust the folder, install rea | [00 Setup](workbooks/00-setup.md) |
| 12:30 – 12:50 | Exercise 1 — **Metaskills**: turn a repeated workflow into a skill | [01 Metaskills](workbooks/01-metaskills.md) |
| 12:50 – 13:10 | Exercise 2 — **Book-to-skill**: turn a book into a queryable expert | [02 Book-to-skill](workbooks/02-book-to-skill.md) |
| 13:10 – 13:30 | Exercise 3 — **Reverse anything**: rebuild a feature from scratch | [03 Reverse anything](workbooks/03-reverse-anything.md) |
| 13:30 – 14:00 | Systems thinking — Claude Code as the gateway to your digital twin | [Slides](presentation/system-thinking/index.html) · [Notes](presentation/system-thinking/source-notes.md) |

## Setup — do this before the session (10 min)

👉 **Follow [00 Setup & installation](workbooks/00-setup.md)**: it installs VSCode, Claude Code, git, Python and Node,
clones this repo, and checks everything works.

Already have everything? Then:

```bash
git clone https://github.com/wukimidaire/claude-code-lunch-and-learn.git
cd claude-code-lunch-and-learn
code .
```

Start Claude Code in that folder, **trust the folder**, and accept the **rea** plugin install.

## What's inside

| Path | What |
|---|---|
| `.claude/skills/` | Skills that load automatically when you open this folder |
| `.claude/settings.json` | Pre-wires the `rea` reverse-engineering plugin |
| `workbooks/` | The three exercises (+ setup) |
| `books/` | A public-domain book for exercise 2 (Sun Tzu, *The Art of War*, Project Gutenberg) |
| `builds/` | Your exercise-3 builds (git-ignored) |
| `presentation/system-thinking/` | Closing presentation — open `index.html` in a browser, use ← → |

### Skills

| Skill | Use it to |
|---|---|
| `/problem-statement` | Distill what the real problem is before solving it |
| `/interview` | Get interviewed until Claude understands what you actually want |
| `/problem-solution` | Wave-based solution search for a confirmed problem |
| `/compare-options` | Structured pros/cons between alternatives |
| `/skill-creator` | Turn a workflow into a reusable `SKILL.md` |
| `/skill-audit` | Check a skill's quality |
| `/book-to-skill` | Convert a PDF/EPUB/DOCX/TXT book into a skill you can query |

## Credits & licences

- **Metaskills** (`interview`, `problem-statement`, `problem-solution`, `compare-options`, `skill-creator`, `skill-audit`) — Nodewin Labs, MIT.
- **book-to-skill** — [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill), MIT (see `.claude/skills/book-to-skill/LICENSE.md`). Vendored unchanged.
- **rea** — [morluto/rea](https://github.com/morluto/rea), MIT. Installed as a plugin, not vendored.
- **The Art of War** — Project Gutenberg eBook #132, public domain in the US.
- Systems-thinking presentation draws on *"How To Think SO Clearly People Assume You're Brilliant"* by Sandeep Swadia (theMITmonk) — [watch it](https://www.youtube.com/watch?v=mjTgkm-h__M).
