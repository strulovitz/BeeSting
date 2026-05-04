"""
Build the University Letter as PLAIN TEXT (UTF-8) from UNIVERSITY_LETTER.md.

When run standalone:
    python generate_letter.py
        Writes the full letter (no batch header) to ~/Downloads/UNIVERSITY_LETTER.txt
        for inspection. Note: generate_batch.py does NOT use this output file —
        it imports build_letter_text() directly so Downloads stays clean.

Conventions in the output:
- Top-level sections (originally **WHOLE-LINE BOLD**) get ROMAN numerals (I, II, ...)
  rendered as:
      I. SECTION TITLE
      ==================
- TOC at the top mirrors EVERY real section heading using the same Roman numerals.
- The 11 numbered industries inside "WHAT CHINA WILL DO WITH IT" keep Arabic numerals
  as "(1)", "(2)", ..., "(11)".
- Inside the FAQ section, "- " bullets become "* " bullets (per Nir's preference).
- Inline **bold** within a sentence becomes ALL-CAPS so emphasis survives plain text.
- Inline *italic* has the asterisks stripped.
- The old opening line ("THE HIVE is a new invention...") is dropped.
"""

import re
from pathlib import Path

REPO = Path(__file__).parent
SRC = REPO / "UNIVERSITY_LETTER.md"
STANDALONE_DST = Path.home() / "Downloads" / "UNIVERSITY_LETTER.txt"

OLD_OPENING = (
    "THE HIVE is a new invention. It is not similar to anything you already know."
)

TOC_TITLE = "What's in this letter:"
EXTRA_UNDERLINE = 10
HEADING_RE = re.compile(r"^[ \t]*\*\*(.+?)\*\*[ \t]*$")


def underline(title: str, ch: str) -> str:
    return ch * (len(title) + EXTRA_UNDERLINE)


def to_roman(n: int) -> str:
    pairs = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    out = ""
    for value, symbol in pairs:
        while n >= value:
            out += symbol
            n -= value
    return out


def transform_inline(line: str) -> str:
    line = re.sub(r"\*\*(.+?)\*\*", lambda m: m.group(1).upper(), line)
    line = re.sub(r"\*(.+?)\*", r"\1", line)
    line = re.sub(r"^([ \t]*)(\d+)\.[ \t]+", r"\1(\2) ", line)
    return line


def build_letter_text(md_text: str) -> str:
    """Transform UNIVERSITY_LETTER.md content into the plain-text letter body."""
    lines = md_text.split("\n")

    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if start_idx is None and line.startswith("Dear ["):
            start_idx = i
        if start_idx is not None and line.strip().startswith("## Recipients"):
            end_idx = i
            break

    if start_idx is None or end_idx is None:
        raise RuntimeError(
            f"Couldn't find letter boundaries: start={start_idx}, end={end_idx}"
        )

    while end_idx > start_idx and lines[end_idx - 1].strip() in ("", "---"):
        end_idx -= 1

    letter_lines = lines[start_idx:end_idx]
    filtered = [l for l in letter_lines if OLD_OPENING not in l]

    section_titles = []
    for line in filtered:
        m = HEADING_RE.match(line)
        if m:
            section_titles.append(m.group(1).strip())

    toc_block = [TOC_TITLE, underline(TOC_TITLE, "-"), ""]
    for i, title in enumerate(section_titles, 1):
        toc_block.append(f"{to_roman(i)}. {title}")
    toc_block.append("")

    output_lines = []
    toc_inserted = False
    section_counter = 0
    in_faq_section = False

    for line in filtered:
        if not toc_inserted and line.startswith("Dear ["):
            output_lines.append(line)
            output_lines.append("")
            output_lines.extend(toc_block)
            toc_inserted = True
            continue

        m = HEADING_RE.match(line)
        if m:
            section_counter += 1
            title = m.group(1).strip()
            full_heading = f"{to_roman(section_counter)}. {title}"
            output_lines.append(full_heading)
            output_lines.append(underline(full_heading, "="))
            in_faq_section = "FAQ" in title.upper()
            continue

        line = transform_inline(line)
        if in_faq_section:
            line = re.sub(r"^([ \t]*)- ", r"\1* ", line)
        output_lines.append(line)

    return "\n".join(output_lines)


def main():
    text = build_letter_text(SRC.read_text(encoding="utf-8"))
    STANDALONE_DST.parent.mkdir(parents=True, exist_ok=True)
    STANDALONE_DST.write_text(text, encoding="utf-8")
    print(f"Wrote {STANDALONE_DST} ({len(text):,} characters)")


if __name__ == "__main__":
    main()
