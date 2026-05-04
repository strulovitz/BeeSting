"""
Generate one paste-ready batch file for the University Letter outreach.

Usage:
    python generate_batch.py <university> <batch_n> <total_batches> <email1,email2,...>

Output: ~/Downloads/UNIVERSITY_LETTER_BATCH_NN.txt
        Top: Subject line, blank, TO: emails, blank, Dear ..., blank, body.

Cleanup: deletes ANY existing ~/Downloads/UNIVERSITY_LETTER*.txt files before
writing the new one, so Downloads only ever holds the current batch.

This script imports build_letter_text() directly from generate_letter.py — no
intermediate UNIVERSITY_LETTER.txt is written to Downloads.
"""

import sys
from pathlib import Path

from generate_letter import SRC, build_letter_text

SUBJECT = (
    "A new kind of AI solves AI alignment but lets China beat America "
    "(including M.A.D.) — now it's your move"
)

DOWNLOADS = Path.home() / "Downloads"


def cleanup_downloads():
    """Delete every UNIVERSITY_LETTER*.txt in Downloads so only the new batch remains."""
    for old in DOWNLOADS.glob("UNIVERSITY_LETTER*.txt"):
        old.unlink()
        print(f"Removed {old.name}")


def main():
    if len(sys.argv) != 5:
        print("Usage: python generate_batch.py <university> <batch_n> <total_batches> <comma_separated_emails>")
        sys.exit(1)

    university = sys.argv[1]
    batch_n = int(sys.argv[2])
    total = int(sys.argv[3])
    emails = [e.strip() for e in sys.argv[4].split(",") if e.strip()]

    body = build_letter_text(SRC.read_text(encoding="utf-8"))

    dear_line = f"Dear {university} Professors (Batch {batch_n} of {total}),"
    if body.startswith("Dear ["):
        nl = body.find("\n")
        body_after_dear = body[nl + 1:]
    else:
        body_after_dear = body

    out = [
        f"Subject: {SUBJECT}",
        "",
        "TO:",
        ", ".join(emails),
        "",
        dear_line,
        body_after_dear.lstrip("\n"),
    ]
    text = "\n".join(out)

    cleanup_downloads()

    dst = DOWNLOADS / f"UNIVERSITY_LETTER_BATCH_{batch_n:02d}.txt"
    dst.write_text(text, encoding="utf-8")
    print(f"Wrote {dst} ({len(text):,} chars, {len(emails)} recipients)")


if __name__ == "__main__":
    main()
