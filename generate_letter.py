"""
Generate the MIT Letter as PLAIN TEXT (UTF-8) from MIT_LETTER.md.

Output: ~/Downloads/MIT_LETTER.txt — ready to paste into Gmail web compose.

Conventions in the output:
- Top-level sections (originally **WHOLE-LINE BOLD**) become:
      SECTION TITLE
      =====================  (length = title length + 10 for proportional-font safety)
- TOC heading uses `-` underline (smaller hierarchy).
- Inline **bold** within a sentence becomes ALL-CAPS so emphasis survives plain text.
- Inline *italic* has the asterisks stripped (just plain text — meaning carries from context).
- Numbered list items "1." "2." become "(1)" "(2)".
- Sub-bullets "- ..." stay as "- ...".
- The old opening line ("THE HIVE is a new invention...") is dropped.
- A 6-entry TOC is inserted right after the salutation (no anchor links — Gmail strips intra-email anchors).
"""

import re
from pathlib import Path

REPO = Path(__file__).parent
SRC = REPO / "MIT_LETTER.md"
DST = Path.home() / "Downloads" / "MIT_LETTER.txt"

OLD_OPENING = (
    "THE HIVE is a new invention. It is not similar to anything you already know."
)

TOC_TITLE = "What's in this letter:"
TOC_ENTRIES = [
    "What the architecture is",
    "How it solves AI alignment",
    "The 10 ways America falls when China deploys it",
    "How it breaks Mutual Assured Destruction",
    "Why this falls to you",
    "Verify everything yourself",
]

# Extra underline beyond the title length, for proportional-font safety
EXTRA_UNDERLINE = 10


def underline(title: str, ch: str) -> str:
    return ch * (len(title) + EXTRA_UNDERLINE)


def main():
    src = SRC.read_text(encoding="utf-8")
    lines = src.split("\n")

    # Find letter boundaries: from "Dear [..." line to "Israel" sign-off line
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
    filtered = [l for l in letter_lines if OLD_OPENING not in l]

    # Build TOC block
    toc_block = []
    toc_block.append(TOC_TITLE)
    toc_block.append(underline(TOC_TITLE, "-"))
    toc_block.append("")
    for i, entry in enumerate(TOC_ENTRIES, 1):
        toc_block.append(f"({i}) {entry}")
    toc_block.append("")

    # Insert TOC right after "Dear [..." line
    new_lines = []
    toc_inserted = False
    for line in filtered:
        new_lines.append(line)
        if not toc_inserted and line.startswith("Dear ["):
            new_lines.append("")
            new_lines.extend(toc_block)
            toc_inserted = True

    text = "\n".join(new_lines)

    # 1) Whole-line **TITLE** -> "TITLE\n=========="  (top-level section heading)
    def heading_replace(match: re.Match) -> str:
        title = match.group(1).strip()
        return f"{title}\n{underline(title, '=')}"

    text = re.sub(
        r"^[ \t]*\*\*(.+?)\*\*[ \t]*$",
        heading_replace,
        text,
        flags=re.MULTILINE,
    )

    # 2) Inline **bold** -> ALL CAPS (after whole-line headings already converted)
    text = re.sub(
        r"\*\*(.+?)\*\*",
        lambda m: m.group(1).upper(),
        text,
        flags=re.DOTALL,
    )

    # 3) Inline *italic* -> strip the asterisks (plain text)
    text = re.sub(r"\*(.+?)\*", r"\1", text, flags=re.DOTALL)

    # 4) Numbered items "1." "2." ... -> "(1) " "(2) " ...
    text = re.sub(
        r"^([ \t]*)(\d+)\.[ \t]+",
        r"\1(\2) ",
        text,
        flags=re.MULTILINE,
    )

    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_text(text, encoding="utf-8")
    print(f"Wrote {DST} ({len(text):,} characters)")


if __name__ == "__main__":
    main()
