"""Render public LinkedIn post summaries as self-contained GitHub SVG cards.
Only edit data/linkedin-posts.json using verified public posts from the owner.
No API tokens, cookies, scraping, external fonts or remote images are needed.
Run: python scripts/render_linkedin.py
"""
import json
import textwrap
from pathlib import Path
from html import escape
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

def render(post):
    url = urlparse(post["url"])
    if url.scheme != "https" or url.hostname not in {"www.linkedin.com", "linkedin.com", "lnkd.in"}:
        raise ValueError("Post links must use HTTPS on LinkedIn or lnkd.in")
    title = textwrap.wrap(post["title"], width=58)[:2]
    lines = textwrap.wrap(post["summary"], width=95)[:2]
    title_svg = "".join(f'<text x="64" y="{140+i*52}" class="title">{escape(t)}</text>' for i,t in enumerate(title))
    summary_y = 212 if len(title) == 1 else 256
    body_svg = "".join(f'<text x="64" y="{summary_y+i*34}" class="body">{escape(t)}</text>' for i,t in enumerate(lines))
    height = 356 if len(title) == 1 else 400
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="{height}" viewBox="0 0 1600 {height}" role="img" aria-label="{escape(post['title'], quote=True)}">
<title>{escape(post['title'])}</title><desc>{escape(post['summary'])}</desc>
<defs><linearGradient id="bg"><stop stop-color="#0b1220"/><stop offset="1" stop-color="#111c32"/></linearGradient><pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse"><path d="M36 0H0V36" fill="none" stroke="#22d3ee" stroke-opacity=".035"/></pattern></defs>
<style>text{{font-family:Segoe UI,Arial,sans-serif}}.title{{font-size:42px;font-weight:700;fill:#edf5ff}}.body{{font-size:26px;fill:#a6b5ce}}</style>
<rect x="1" y="1" width="1598" height="{height-2}" rx="24" fill="url(#bg)" stroke="#263852"/><rect width="1600" height="{height}" fill="url(#grid)" rx="24"/>
<rect x="1" y="24" width="5" height="{height-48}" rx="2" fill="#22d3ee"/>
<text x="64" y="65" fill="#22d3ee" font-size="19" letter-spacing="3">{escape(post['category'])}</text>
<rect x="1390" y="40" width="150" height="36" rx="18" fill="#22d3ee" fill-opacity=".10"/><text x="1465" y="65" text-anchor="middle" font-size="18" fill="#a5b4fc">{escape(post['date'])}</text>
{title_svg}{body_svg}
<line x1="64" y1="{height-78}" x2="1536" y2="{height-78}" stroke="#263852"/>
<text x="64" y="{height-35}" font-size="20" fill="#94a3b8">Kavindu Oshadha Perera · LinkedIn</text><text x="1536" y="{height-35}" text-anchor="end" font-size="21" fill="#22d3ee">Read the post ↗</text>
</svg>'''

def main():
    posts = json.loads((ROOT / "data/linkedin-posts.json").read_text(encoding="utf-8"))
    if not isinstance(posts, list) or not 1 <= len(posts) <= 3:
        raise ValueError("Expected one to three verified posts")
    ids = [p["id"] for p in posts]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate post identifiers")
    target = ROOT / "assets"
    target.mkdir(exist_ok=True)
    for i, post in enumerate(posts, 1):
        (target / f"linkedin-post-{i}.svg").write_text(render(post), encoding="utf-8")
    for i in range(len(posts) + 1, 4):
        (target / f"linkedin-post-{i}.svg").unlink(missing_ok=True)

if __name__ == "__main__":
    main()
