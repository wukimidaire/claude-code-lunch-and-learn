# 00 — Setup & installation (10 min — ideally **before** the session)

Goal: this repo open in VSCode, Claude Code running inside it, and every tool the 3 exercises need installed.

## Step 1 — Check what you already have (2 min)

Open a terminal (VSCode: **Terminal → New Terminal**) and run:

```bash
git --version      # any version
python3 --version  # 3.9 or newer   (Windows: python --version)
node -v            # v22 or newer   (only needed for exercise 3)
claude --version   # Claude Code CLI (optional if you use the VSCode extension)
```

✅ All four print a version → go to Step 3.
❌ Something says `command not found` → Step 2 for that tool only.

## Step 2 — Install what's missing (5 min)

| Tool | macOS | Windows | Why |
|---|---|---|---|
| **VSCode** | [code.visualstudio.com](https://code.visualstudio.com) | same | Your editor |
| **Claude Code** | VSCode → Extensions (`Cmd+Shift+X`) → search **Claude Code** → Install → sign in | same (`Ctrl+Shift+X`) | The agent. Needs a Claude Pro/Max/Team plan |
| **git** | `xcode-select --install` | [git-scm.com/download/win](https://git-scm.com/download/win) | Clone this repo |
| **Python 3** | `brew install python` or [python.org](https://www.python.org/downloads/) | [python.org](https://www.python.org/downloads/) — tick **"Add to PATH"** | Exercise 2 (book-to-skill) |
| **Node.js 22+** | `brew install node` or [nodejs.org](https://nodejs.org) (LTS) | [nodejs.org](https://nodejs.org) (LTS) | Exercise 3 (rea) |

> No Homebrew on Mac? Use the website installers — they work just as well.
> After installing anything: **close and reopen VSCode** so the terminal picks it up.

## Step 3 — Clone this repo into VSCode (1 min)

**Option A — no terminal:** in VSCode press `Cmd+Shift+P` (Windows `Ctrl+Shift+P`) → **Git: Clone** → paste
`https://github.com/wukimidaire/claude-code-lunch-and-learn.git` → pick a folder → **Open**.

**Option B — terminal:**

```bash
git clone https://github.com/wukimidaire/claude-code-lunch-and-learn.git
cd claude-code-lunch-and-learn
code .
```

> Claude Code must be started **inside this folder** — that's how it finds the workshop skills.

## Step 4 — Start Claude Code and trust the folder (1 min)

- Click the **Claude Code** icon in the VSCode sidebar, or type `claude` in the VSCode terminal.
- When asked *"Do you trust the files in this folder?"* → **Yes**.
- When asked to install the **rea** plugin (from `morluto/rea`) → **Yes / Install**, then restart Claude Code.

## Step 5 — Install rea manually (only if you weren't asked in Step 4)

Inside Claude Code type:

```
/plugin marketplace add morluto/rea
/plugin install rea@rea
```

Restart Claude Code. Still failing? In a terminal: `npx rea-agents setup` → choose **Claude Code** → restart.
Use **one** route only — doing both gives you two `rea` servers.

## Step 6 — Verify (1 min)

Paste this into Claude Code:

> **Check my workshop setup: list the skills and MCP servers available in this project, and run
> `python3 --version`, `node -v` and `python3 .claude/skills/book-to-skill/scripts/extract.py --check`.
> Tell me what's missing and how to fix it.**

- [ ] Typing `/` shows `problem-statement`, `interview`, `skill-creator`, `skill-audit`, `book-to-skill`…
- [ ] `/mcp` lists **rea** as connected
- [ ] The extractor check runs (missing *optional* packages are fine)

## Troubleshooting

| Problem | Fix |
|---|---|
| Skills don't show up when typing `/` | Claude Code was started outside the repo folder. Open the folder in VSCode (**File → Open Folder**) and restart Claude Code |
| `python3` not found on Windows | Use `python` instead, or reinstall Python with **"Add to PATH"** ticked |
| `node -v` shows v18 or v20 | Install the current LTS from nodejs.org, reopen VSCode |
| rea shows as failed in `/mcp` | `node -v` must be 22+; restart Claude Code after installing Node |
| Claude Code asks you to log in | Sign in with your Claude account (Pro/Max/Team needed) |
| Stuck for more than 3 minutes | Raise your hand. Do exercises 1 and 2 meanwhile — they don't need Node |

➡️ Next: [01 Metaskills](01-metaskills.md)
