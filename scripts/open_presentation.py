"""Open the systems-thinking presentation in your default browser.

Usage:  python3 scripts/open_presentation.py [slide-number]
        (Windows: python scripts\\open_presentation.py)
"""
import pathlib, sys, webbrowser

DECK = pathlib.Path(__file__).resolve().parent.parent / "presentation" / "system-thinking" / "index.html"

if not DECK.exists():
    sys.exit(f"Presentation not found at {DECK}. Run this from inside the cloned repo.")

slide = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].isdigit() else "1"
url = f"{DECK.as_uri()}#{slide}"
print(f"Opening {url}")
if not webbrowser.open(url):
    print("Could not open a browser automatically. Paste the URL above into your browser.")
