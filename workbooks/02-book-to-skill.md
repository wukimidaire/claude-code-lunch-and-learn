# 02 — Book-to-skill: turn a book into an expert you can query (20 min)

## Prerequisites

- [ ] [01 Metaskills](01-metaskills.md) done (or at least setup)
- [ ] Python 3
- [ ] A book: use `books/sun-tzu-art-of-war.txt`, or bring your own PDF/EPUB/DOCX **you legally own**

## What you will build

A skill generated from a book — an index `SKILL.md` plus chapter files, glossary, patterns and a cheatsheet —
that you can ask questions and apply to your own work.

## Steps

| Min | Step | What to type |
|---|---|---|
| 0–2 | **Check the extractor** | In the terminal: `python3 .claude/skills/book-to-skill/scripts/extract.py --check` |
| 2–10 | **Convert the book** | `/book-to-skill books/sun-tzu-art-of-war.txt` (or the path to your own book). Answer its questions. |
| 10–13 | **Look at what it built** | Ask Claude: "Where did you write the skill and what's in it?" Open the `SKILL.md` |
| 13–18 | **Query the expert** | `/<book-skill> <topic>` — e.g. `/art-of-war how do I pick battles with competitors?` |
| 18–20 | **Apply it** | Combine it with exercise 1: "Use the book skill to improve my `<name>` skill" |

> **Where does it go?** By default book-to-skill writes to your personal skills (`~/.agents/skills/<slug>/`, linked into `~/.claude/skills/`).
> Want it in this repo instead? Run with `BOOK_TO_SKILL_SCOPE=project`.

## If something goes wrong

| Problem | Fix |
|---|---|
| PDF extraction fails | `pip install pypdf` or `brew install poppler` — or use the `.txt` book in `books/` |
| Scanned PDF (images only) | Needs OCR first (`ocrmypdf`) — use another book today |
| Takes too long | Ask Claude to convert only the first chapters for now |

## Verification

- [ ] A new skill folder with `SKILL.md` exists
- [ ] Querying it gives answers that cite the book's chapters

## Why this matters

Expertise in books is **complicated, not complex**: the answer exists, you just need the right specialist.
book-to-skill gives you that specialist on demand.

## Take-home

- Convert the 3 books that shaped how your company works (sales, ops, strategy)
- Install it anywhere: `npx skills add virgiliojr94/book-to-skill` · source: <https://github.com/virgiliojr94/book-to-skill>

➡️ Next: [03 Reverse anything](03-reverse-anything.md)
