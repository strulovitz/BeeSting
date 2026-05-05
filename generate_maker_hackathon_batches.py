"""
Build the Maker/Hackathon Letter as PLAIN TEXT and generate batches of 20 emails each.

Source: ~/Downloads/UNIVERSITY_LETTER.txt (must be regenerated from UNIVERSITY_LETTER.md
        via `python generate_letter.py` if it doesn't exist or is outdated).

Modifications applied:
  - Section V word substitution
  - Section VI word substitution
  - Section XI word substitution
  - Section VII fully rewritten ("audience IS the hive" demo)
  - New "+ FOR YOU SPECIFICALLY" perk block inserted before Section XII

Recipient list: parsed from BeeSting/MAKER_HACKATHON_LETTER.md
                (every line matching `- \\`email@domain\\` — ...`)

Output: ~/Downloads/MAKER_HACKATHON_LETTER_BATCH_01.txt … _NN.txt
        Each: Subject + To: + Dear line + body
"""

import re
from pathlib import Path

REPO = Path(__file__).parent
DOWNLOADS = Path.home() / "Downloads"
SOURCE_TXT = DOWNLOADS / "UNIVERSITY_LETTER.txt"
RECIPIENTS_MD = REPO / "MAKER_HACKATHON_LETTER.md"

SUBJECT = (
    "A new kind of AI solves AI alignment but lets China beat America "
    "(including M.A.D.) — now it's your move"
)

BATCH_SIZE = 20

# --- Word substitutions in Sections V, VI, XI ---
WORD_SUBSTITUTIONS = [
    (
        "the same demonstration your university can run for the parallelism and quality benchmarks",
        "the same demonstration your event can run for the parallelism and quality benchmarks",
    ),
    (
        "For your university, this is the worst strategic outcome since 1945",
        "For America, this is the worst strategic outcome since 1945",
    ),
    (
        "A friendly university proves to America's power centers above that THE HIVE is not a dream",
        "A friendly maker, hackathon, or hardware-hacker event proves to America's power centers above that THE HIVE is not a dream",
    ),
]

# --- Section VII rewrite ---
NEW_SECTION_VII = """VII. HOW YOU CAN SAVE AMERICA TODAY FOR FREE
========================================================

I have been writing to journalists, professors, defense contractors, Big AI labs, and government bodies for weeks. Auto-replies confirm delivery. The silence tells me the asymmetry between an outside individual and a civilizational claim is too large for any single recipient to act on alone.

Without a small live demonstration on real hardware — not a 15-virtual-machine cluster across two consumer desktops — the first AND last demonstration America will see is China activating THE HIVE at full national scale.

Your role here is precise and limited. YOUR EVENT IS NOT THE JUDGE OF THE HIVE. THE JUDGE WILL BE HISTORY — IF YOU FAIL. What you provide is the LIVE DEMONSTRATION at your event — where your audience IS the hive. We bring the demo. You provide the venue, the audience, and the network. America's institutions — e.g. Big AI, the Pentagon, NSA, cyber defense, Big Pharma, Wall Street, defense contractors, drone manufacturers, the strategic submarine fleet, robotics, and homeland security — see a working architecture in advance, instead of meeting the big real-life deadly test that takes them all out together. You serve as the KNOWLEDGE MEDIATOR between an outsider with a working architecture and the rest of America.

The setup: the audience runs HIVE on whatever they brought. Most maker, hackathon, and Hackaday-style laptops (ThinkPad, Framework, gaming-class Lenovo / ASUS / MSI) have built-in Ethernet and plug straight into the venue's switching. The Apple/ultrabook minority joins the same network over WiFi or via a USB-C-to-Ethernet adapter from our stock. The same hive protocol runs across both. Typical scale: 30–100 audience laptops on a standard venue setup; 200–500 on enterprise WiFi or LAN such as a major hackathon's existing infrastructure. We adapt to the network your venue already has, and the heterogeneity itself is realistic — it mirrors HIVE's actual deployment model: consumer machines on whatever network they happen to be on.

The cost to you is small: one stage time slot or one hackathon track. Real hardware. Real audience. Real demonstration — comparable against any frontier Big AI cloud on both TIMING AND QUALITY, in front of the audience, in real time. A five-minute sanity check can come first — ask any frontier cloud AI assistant to read the GitHub repositories and confirm the architecture is real and works as described.

If no major maker, hackathon, or hardware-hacker event in America hosts that small live demo in time, history's verdict is binary: America became history — e.g. in Big AI, the Pentagon, NSA, cyber defense, Big Pharma, Wall Street, defense contractors, drone manufacturers, the strategic submarine fleet, robotics, and homeland security. There is no second chance.

This is your chance to be American heroes who save your nation. Think of it as a Hackathon where the grand prize is your country's life.
"""

# --- "+ for you specifically" perk block ---
PERK_BLOCK = """+ FOR YOU SPECIFICALLY — WHY HOSTING THIS DEMO IS WORTH YOUR EVENT'S TIME
============================================================================

Beyond the universal stakes above, here is what hosting this demo gives your event in particular.

You become the first event in the world where the audience runs THE HIVE. The architecture is on GitHub today and the rest of the world will catch on within months — but only one event gets to be the venue where it was shown publicly first. There is exactly one of those slots. Everything after is "the second time," "the third time," "the tenth time." Once that slot is taken, it is taken. There is no way to be first twice.

Your audience does not run a toy demo. Maker-culture kids and hackathon students reject toy demos on sight — they have built radios and drones and robots, and they recognize hollow projects in five minutes. THE HIVE is not hollow. A hive of this kind functions in environments where centralized cloud AI cannot: a Mars colony in the middle of a six-month dust-storm communication blackout where the crew cannot contact Earth at all; a Europa or Titan mission where each command takes hours each way; a spacecraft triaging a medical emergency in real time; calculating how much oxygen the crew needs from minute to minute; treating the plants that are the food of the crew when something goes wrong with them.

The bee-and-honey metaphor every kid already loves works as the architecture's natural language. Workers, DwarfQueens, GiantQueens, RajaBee — none of these need to be explained. Every kid in your room understands a hive on the day they walk in. That is effortless cognitive uptake — kids GET it without slides, without diagrams, without prerequisite math. They become participants the moment they sit down.

The kids walk out of your event understanding something most adults do not yet understand. Most senators do not understand it. Most AI researchers outside of a handful of labs do not understand it. The kids in your room do — because they were the architecture for an hour. That is structural empowerment. It is the rarest gift a maker event can give a kid: not knowledge of an old technology, but participation in a new one before the public catches up. There is nothing cooler a kid can take home.

"""


def parse_emails_from_recipients_md() -> list[str]:
    """Extract every verified email from MAKER_HACKATHON_LETTER.md.
    Pattern: lines like `- ` + ``` ` ``` + email + ``` ` ``` + ` — description`."""
    text = RECIPIENTS_MD.read_text(encoding="utf-8")
    emails: list[str] = []
    seen: set[str] = set()
    pattern = re.compile(r"^- `([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})`", re.MULTILINE)
    for m in pattern.finditer(text):
        email = m.group(1)
        if email not in seen:
            seen.add(email)
            emails.append(email)
    return emails


def build_maker_hackathon_text(university_text: str) -> str:
    """Apply maker/hackathon transformations to the university plaintext."""
    text = university_text

    # Word substitutions
    for old, new in WORD_SUBSTITUTIONS:
        if old not in text:
            raise ValueError(f"Substitution miss — couldn't find:\n  {old!r}")
        text = text.replace(old, new)

    # Replace Section VII
    section_vii_pattern = re.compile(
        r"VII\. HOW YOU CAN SAVE AMERICA TODAY FOR FREE.*?(?=VIII\. THE OPENCLAW)",
        re.DOTALL,
    )
    if not section_vii_pattern.search(text):
        raise ValueError("Section VII pattern not found in source text.")
    text = section_vii_pattern.sub(NEW_SECTION_VII + "\n\n", text)

    # Insert perk block before Section XII
    section_xii_marker = "XII. THE STAKES IF THIS DOES NOT HAPPEN SOON"
    if section_xii_marker not in text:
        raise ValueError(f"Section XII marker not found: {section_xii_marker!r}")
    text = text.replace(section_xii_marker, PERK_BLOCK + section_xii_marker)

    return text


def cleanup_old_batches() -> None:
    for old in DOWNLOADS.glob("MAKER_HACKATHON_LETTER_BATCH*.txt"):
        old.unlink()
        print(f"Removed {old.name}")


def main() -> None:
    if not SOURCE_TXT.exists():
        raise SystemExit(
            f"Source not found: {SOURCE_TXT}\n"
            "Run `python generate_letter.py` first to produce UNIVERSITY_LETTER.txt."
        )

    base_text = SOURCE_TXT.read_text(encoding="utf-8")
    body = build_maker_hackathon_text(base_text)

    # Strip the original "Dear [Names — to be filled per recipient list]," line
    body_after_dear = re.sub(r"^Dear \[Names[^\n]*\],?\s*\n", "", body, count=1)

    emails = parse_emails_from_recipients_md()
    if not emails:
        raise SystemExit("No emails parsed from MAKER_HACKATHON_LETTER.md.")

    batches = [emails[i : i + BATCH_SIZE] for i in range(0, len(emails), BATCH_SIZE)]
    total_batches = len(batches)

    cleanup_old_batches()

    for batch_n, batch_emails in enumerate(batches, start=1):
        dear_line = (
            f"Dear maker, hackathon, and youth-tech event organizer "
            f"(Batch {batch_n} of {total_batches}),"
        )
        out_lines = [
            f"Subject: {SUBJECT}",
            "",
            "TO:",
            ", ".join(batch_emails),
            "",
            dear_line,
            body_after_dear.lstrip("\n"),
        ]
        out_text = "\n".join(out_lines)
        dst = DOWNLOADS / f"MAKER_HACKATHON_LETTER_BATCH_{batch_n:02d}.txt"
        dst.write_text(out_text, encoding="utf-8")
        print(f"Wrote {dst.name} ({len(out_text):,} chars, {len(batch_emails)} recipients)")

    print(f"\n{total_batches} batches generated covering {len(emails)} unique emails.")


if __name__ == "__main__":
    main()
