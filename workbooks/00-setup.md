# 00 — Setup (5 min)

## Checklist

- [ ] Repo cloned and opened in VSCode (`code .` from the repo folder)
- [ ] Claude Code open in this folder, folder **trusted**
- [ ] Skills visible: type `/` and look for `problem-statement`, `interview`, `skill-creator`, `book-to-skill`
- [ ] Python works: `python3 --version`
- [ ] Node 22+: `node -v` (needed for exercise 3)
- [ ] rea plugin active: run `/mcp` → `rea` is listed as connected

## If something is missing

| Problem | Fix |
|---|---|
| Skills don't show up | Make sure Claude Code was started **inside** the repo folder. Restart it. |
| No prompt to install rea | In Claude Code: `/plugin marketplace add morluto/rea` then `/plugin install rea@rea`, restart |
| `/plugin` route fails | In a terminal: `npx rea-agents setup`, choose Claude Code, restart. (Use one route, not both — otherwise you get two `rea` servers.) |
| Node older than 22 | Install the LTS from nodejs.org — or do exercise 3 with the *no-rea fallback* |

## Verification

Ask Claude: **"Which skills and MCP servers are available in this project?"** — you should see the 7 skills and `rea`.

➡️ Next: [01 Metaskills](01-metaskills.md)
