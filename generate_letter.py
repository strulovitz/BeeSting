"""
Generate the University Letter as PLAIN TEXT (UTF-8) from UNIVERSITY_LETTER.md.

Output: ~/Downloads/UNIVERSITY_LETTER.txt — ready to paste into Gmail web compose.

Conventions in the output:
- Top-level sections (originally **WHOLE-LINE BOLD**) are numbered with ROMAN numerals
  (I, II, III, ...) and rendered as:
      I. SECTION TITLE
      ==================
- TOC at the top mirrors EVERY real section heading (no grouping or invented entries),
  using the same Roman numerals.
- The 11 numbered industries inside the "WHAT CHINA WILL DO WITH IT" section keep their
  Arabic numerals as "(1)" "(2)" ... "(11)".
- Inside the FAQ section, "- " bullets become "* " bullets (per Nir's preference).
- Inline **bold** within a sentence becomes ALL-CAPS so emphasis survives plain text.
- Inline *italic* has the asterisks stripped.
- The old opening line ("THE HIVE is a new invention...") is dropped.
"""

import re
from pathlib import Path

REPO = Path(__file__).parent
SRC = REPO / "UNIVERSITY_LETTER.md"
DST = Path.home() / "Downloads" / "UNIVERSITY_LETTER.txt"

OLD_OPENING = (
    "THE HIVE is a new invention. It is not similar to anything you already know."
)

TOC_TITLE = "What's in this letter:"

# Extra underline beyond the title length, for proportional-font safety
EXTRA_UNDERLINE = 10

# Pattern for whole-line bold heading: **TITLE**
HEADING_RE = re.compile(r"^[ \t]*\*\*(.+?)\*\*[ \t]*$")


def underline(title: str, ch: str) -> str:
    return ch * (len(title) + EXTRA_UNDERLINE)


def to_roman(n: int) -> str:
    """Convert positive integer to Roman numeral."""
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
    """Apply inline transformations: **bold** -> ALL CAPS, *italic* -> plain, '1.' -> '(1) '."""
    line = re.sub(r"\*\*(.+?)\*\*", lambda m: m.group(1).upper(), line)
    line = re.sub(r"\*(.+?)\*", r"\1", line)
    line = re.sub(r"^([ \t]*)(\d+)\.[ \t]+", r"\1(\2) ", line)
    return line


def main():
    src = SRC.read_text(encoding="utf-8")
    lines = src.split("\n")

    # Find letter boundaries: from "Dear [..." to before "## Recipients"
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

    # Trim trailing blank lines and "---" separators
    while end_idx > start_idx and lines[end_idx - 1].strip() in ("", "---"):
        end_idx -= 1

    letter_lines = lines[start_idx:end_idx]

    # Drop the old opening line
    filtered = [l for l in letter_lines if OLD_OPENING not in l]

    # First pass: collect every real section heading (whole-line bold)
    section_titles = []
    for line in filtered:
        m = HEADING_RE.match(line)
        if m:
            section_titles.append(m.group(1).strip())

    # Build TOC with Roman numerals (one entry per real section, no grouping)
    toc_block = []
    toc_block.append(TOC_TITLE)
    toc_block.append(underline(TOC_TITLE, "-"))
    toc_block.append("")
    for i, title in enumerate(section_titles, 1):
        roman = to_roman(i)
        toc_block.append(f"{roman}. {title}")
    toc_block.append("")

    # Second pass: build output, transforming as we go
    output_lines = []
    toc_inserted = False
    section_counter = 0
    in_faq_section = False

    for line in filtered:
        # Insert TOC right after "Dear [..." line
        if not toc_inserted and line.startswith("Dear ["):
            output_lines.append(line)
            output_lines.append("")
            output_lines.extend(toc_block)
            toc_inserted = True
            continue

        # Whole-line bold heading -> Roman numeral + title + === underline
        m = HEADING_RE.match(line)
        if m:
            section_counter += 1
            title = m.group(1).strip()
            roman = to_roman(section_counter)
            full_heading = f"{roman}. {title}"
            output_lines.append(full_heading)
            output_lines.append(underline(full_heading, "="))
            in_faq_section = "FAQ" in title.upper()
            continue

        # Inline transformations FIRST (while bullets are still "- "; otherwise the
        # italic-strip regex would match a leading "* " bullet as the start of italics)
        line = transform_inline(line)

        # FAQ section: NOW convert "- " bullets to "* " bullets, after italics are processed
        if in_faq_section:
            line = re.sub(r"^([ \t]*)- ", r"\1* ", line)

        output_lines.append(line)

    text = "\n".join(output_lines)

    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_text(text, encoding="utf-8")
    print(f"Wrote {DST} ({len(text):,} characters)")


if __name__ == "__main__":
    main()
