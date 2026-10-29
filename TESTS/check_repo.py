"""Repo checks for the lunch & learn repo. Run: python3 TESTS/check_repo.py"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ["interview", "problem-statement", "problem-solution", "compare-options",
          "skill-creator", "skill-audit", "book-to-skill"]
PRIVATE = re.compile(r"\b(?:azumuta|aikido|conveo|cuez|arplama|otiv|volta|kappa|eagl|victor|/Users/|"
                     r"client_projects|sk-ant-|ghp_|service_role|keynote\.pptx)", re.I)
VENDORED = {"book-to-skill", "books"}  # third-party upstream content, scanned only for secrets
TEXT = {".md", ".html", ".json", ".yaml", ".yml", ".txt", ".py"}
errors = []

for s in SKILLS:
    f = ROOT / ".claude/skills" / s / "SKILL.md"
    if not f.exists():
        errors.append(f"missing skill {s}"); continue
    head = f.read_text().split("---")[1] if f.read_text().startswith("---") else ""
    if "name:" not in head or "description:" not in head:
        errors.append(f"bad frontmatter {s}")
if not list((ROOT / ".claude/skills/book-to-skill").glob("LICENSE*")):
    errors.append("book-to-skill LICENSE missing")

settings = ROOT / ".claude/settings.json"
if not settings.exists() or "rea@rea" not in settings.read_text():
    errors.append("rea plugin not wired in .claude/settings.json")

for md in [ROOT / "README.md", *sorted((ROOT / "workbooks").glob("*.md"))]:
    if not md.exists():
        errors.append(f"missing {md.relative_to(ROOT)}"); continue
    for link in re.findall(r"\]\(([^)#]+)", md.read_text()):
        if not link.startswith("http") and not (md.parent / link).exists():
            errors.append(f"broken link {link} in {md.name}")
for wb in ["00-setup", "01-metaskills", "02-book-to-skill", "03-reverse-anything"]:
    if not (ROOT / "workbooks" / f"{wb}.md").exists():
        errors.append(f"missing workbook {wb}")

deck = ROOT / "presentation/system-thinking/index.html"
if not deck.exists() or deck.read_text().count('<section class="slide') < 14:
    errors.append("slide deck missing or < 14 slides")
deck_text = deck.read_text() if deck.exists() else ""
if "Hermes" not in deck_text or "agent operating system" not in deck_text.lower():
    errors.append("deck has no Hermes agent-OS slide")
opener = ROOT / "scripts/open_presentation.py"
if not opener.exists():
    errors.append("missing scripts/open_presentation.py")
if "scripts/open_presentation.py" not in (ROOT / "workbooks/03-reverse-anything.md").read_text():
    errors.append("WB03 does not run the presentation opener")
if not list((ROOT / "books").glob("*.txt")):
    errors.append("no sample book")

for f in ROOT.rglob("*"):
    if f.is_file() and f.suffix in TEXT and ".git" not in f.parts and f.name != "check_repo.py" \
            and not VENDORED & set(f.parts):
        for i, line in enumerate(f.read_text(errors="ignore").splitlines(), 1):
            if PRIVATE.search(line):
                errors.append(f"private string {f.relative_to(ROOT)}:{i}: {line.strip()[:80]}")

print("\n".join(errors) or "ALL CHECKS PASS")
sys.exit(1 if errors else 0)
