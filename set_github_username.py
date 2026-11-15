"""Replace the YOUR-GITHUB-USERNAME placeholder in notebooks and Markdown files.

Usage (from the repository root):
    python scripts/set_github_username.py your-github-username
"""
import pathlib
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python scripts/set_github_username.py <github-username>")
user = sys.argv[1].strip()
root = pathlib.Path(__file__).resolve().parent.parent
changed = 0
for path in list(root.rglob("*.ipynb")) + list(root.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    if "YOUR-GITHUB-USERNAME" in text:
        path.write_text(text.replace("YOUR-GITHUB-USERNAME", user), encoding="utf-8")
        changed += 1
print(f"Updated {changed} files for github.com/{user}")
