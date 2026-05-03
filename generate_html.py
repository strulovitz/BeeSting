"""
Generate MIT_LETTER.html from MIT_LETTER.md with TOC + anchor links.

Usage: python generate_html.py

Output: MIT_LETTER.html in the same directory.
- Strips admin frontmatter (everything before "Dear [Names...]")
- Strips admin section after "Israel" sign-off
- Drops the old opening line ("THE HIVE is a new invention. It is not similar to anything you already know.")
- Inserts a TOC right after the salutation, with anchor links to the 6 main sections
- Adds id attributes to the bold section headings
- Converts markdown to HTML

Then: open MIT_LETTER.html in a browser, Ctrl+A, Ctrl+C, paste into Thunderbird compose.
"""

from pathlib import Path
import markdown

REPO = Path(__file__).parent
SRC = REPO / "MIT_LETTER.md"
DST = Path.home() / "Downloads" / "MIT_LETTER.html"

# Section bold-headings → anchor IDs
SECTION_ANCHORS = {
    "WHAT THE HIVE IS — IN PLAIN ENGLISH": "architecture",
    "WHAT CHINA WILL DO WITH IT": "china-falls",
    "FAQ — IT IS NOT WHAT YOU ALREADY KNOW": "faq",
    "HOW IT WORKS — TECHNICAL": "how-it-works",
    "THE HIVE SOLVES THE ALIGNMENT PROBLEM": "alignment",
    "HOW THE HIVE ENDS AMERICAN SECOND-STRIKE CAPABILITY AND BREAKS MAD": "mad",
    "THE WALL — AND WHY MIT IS THE WAY THROUGH IT": "why-you",
    "THE OPENCLAW / MOLTBOOK PRECEDENT": "precedent",
    "THE CHINESE EMBASSY — AS A LOGICAL NEXT STEP": "embassy",
    "THE PREFERRED PATH": "preferred",
    "THE STAKES IF THIS DOES NOT HAPPEN SOON": "stakes",
    "FOR THOSE WHO THINK I EXAGGERATE": "verify-book",
    "LINKS": "links",
}

# 6 TOC entries → anchor IDs (each maps to the START of a logical section group)
TOC_ENTRIES = [
    ("What the architecture is", "architecture"),
    ("How it solves alignment", "alignment"),
    ("The 10 ways America falls when China deploys it", "china-falls"),
    ("How it breaks Mutual Assured Destruction", "mad"),
    ("Why this falls to you", "why-you"),
    ("Verify everything yourself", "links"),
]


def main():
    src = SRC.read_text(encoding="utf-8")
    lines = src.split("\n")

    # Find the letter portion: from "Dear [..." to "Israel" sign-off
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if line.startswith("Dear ["):
            start_idx = i
        if start_idx is not None and end_idx is None and line.strip() == "Israel":
            end_idx = i + 1
            break

    if start_idx is None or end_idx is None:
        raise RuntimeError(
            f"Couldn't find letter boundaries: start={start_idx}, end={end_idx}"
        )

    letter_lines = lines[start_idx:end_idx]

    # Drop the old opening line
    OLD_OPENING = (
        "THE HIVE is a new invention. It is not similar to anything you already know."
    )
    filtered = [l for l in letter_lines if OLD_OPENING not in l]

    # Normalize sub-bullet indentation: convert 3-space-indent bullets ("   - ")
    # to 4-space-indent ("    - ") so python-markdown nests them inside numbered
    # items consistently (items 1-9 used 3 spaces, items 10-11 used 4 spaces).
    normalized = []
    for line in filtered:
        if line.startswith("   - ") and not line.startswith("    - "):
            normalized.append(" " + line)  # 3 → 4
        else:
            normalized.append(line)
    filtered = normalized

    # Replace **SECTION TITLE** lines with HTML <h2 id="...">...</h2>
    rewritten = []
    for line in filtered:
        stripped = line.strip()
        replaced = False
        for title, aid in SECTION_ANCHORS.items():
            if stripped == f"**{title}**":
                rewritten.append(f'<h2 id="{aid}">{title}</h2>')
                replaced = True
                break
        if not replaced:
            rewritten.append(line)

    # Build TOC HTML
    toc_html = ['<h2>What\'s in this letter (8 minutes):</h2>', "<ol>"]
    for label, aid in TOC_ENTRIES:
        toc_html.append(f'  <li><a href="#{aid}">{label}</a></li>')
    toc_html.append("</ol>")
    toc_html_str = "\n".join(toc_html)

    # Insert TOC right after the "Dear [..." line
    final_lines = []
    toc_inserted = False
    for line in rewritten:
        final_lines.append(line)
        if not toc_inserted and line.startswith("Dear ["):
            final_lines.append("")
            final_lines.append(toc_html_str)
            final_lines.append("")
            toc_inserted = True

    letter_md = "\n".join(final_lines)

    # Convert markdown to HTML (the 'extra' extension handles inline HTML and tables)
    html_body = markdown.markdown(letter_md, extensions=["extra"])

    # Wrap in a full HTML document
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>MIT Letter</title>
<style>
body {{ font-family: Georgia, 'Times New Roman', serif; max-width: 760px; margin: 2em auto; padding: 0 1em; line-height: 1.55; color: #111; }}
h2 {{ margin-top: 2em; }}
ol, ul {{ padding-left: 1.5em; }}
li {{ margin-bottom: 0.4em; }}
a {{ color: #1a5fa3; }}
blockquote {{ border-left: 3px solid #999; padding-left: 1em; color: #444; }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

    DST.write_text(html, encoding="utf-8")
    print(f"Wrote {DST} ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
