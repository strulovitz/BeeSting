"""
Generate one paste-ready batch file for the University Letter outreach.

Usage:
    python generate_batch.py <university> <batch_n> <total_batches> <email1,email2,...>

Output: ~/Downloads/UNIVERSITY_LETTER_BATCH_NN.txt
        Top: Subject line, blank, TO: emails, blank, Dear ..., blank, body.
        Body is taken from ~/Downloads/UNIVERSITY_LETTER.txt (regenerate first if stale).
"""

import sys
from pathlib import Path

SUBJECT = (
    "A new kind of AI solves AI alignment but lets China beat America "
    "(including M.A.D.) — now it's your move"
)

DOWNLOADS = Path.home() / "Downloads"
SRC = DOWNLOADS / "UNIVERSITY_LETTER.txt"


def main():
    if len(sys.argv) != 5:
        print("Usage: python generate_batch.py <university> <batch_n> <total_batches> <comma_separated_emails>")
        sys.exit(1)

    university = sys.argv[1]          # e.g. "MIT EECS"
    batch_n = int(sys.argv[2])
    total = int(sys.argv[3])
    emails = [e.strip() for e in sys.argv[4].split(",") if e.strip()]

    body = SRC.read_text(encoding="utf-8")
    # Replace placeholder Dear line with personalized one
    dear_line = f"Dear {university} Professors (Batch {batch_n} of {total}),"
    if body.startswith("Dear ["):
        nl = body.find("\n")
        body_after_dear = body[nl + 1:]
    else:
        body_after_dear = body

    out = []
    out.append(f"Subject: {SUBJECT}")
    out.append("")
    out.append("TO:")
    out.append(", ".join(emails))
    out.append("")
    out.append(dear_line)
    out.append(body_after_dear.lstrip("\n"))

    text = "\n".join(out)
    dst = DOWNLOADS / f"UNIVERSITY_LETTER_BATCH_{batch_n:02d}.txt"
    dst.write_text(text, encoding="utf-8")
    print(f"Wrote {dst} ({len(text):,} chars, {len(emails)} recipients)")


if __name__ == "__main__":
    main()
