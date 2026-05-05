"""
Generate ONE Maker/Hackathon Letter batch at a time.

Usage:
    python generate_maker_hackathon_batches.py <batch_n>

Writes a SINGLE file to Downloads:
    ~/Downloads/MAKER_HACKATHON_LETTER_BATCH_NN.txt

Cleans up any prior MAKER_HACKATHON_LETTER_BATCH*.txt in Downloads first, so
Nir always sees exactly one file at a time (he has ADD; multiple files cause
confusion). Pattern mirrored from BeeSting/generate_batch.py.

Source plaintext:    ~/Downloads/UNIVERSITY_LETTER.txt
                     (regenerate with `python generate_letter.py` if missing)

Recipient list:      BeeSting/MAKER_HACKATHON_LETTER.md
                     (every line `- \\`email@domain\\` — ...`)

Modifications applied (vs. university letter):
  - Section V word substitution
  - Section VI word substitution
  - Section XI word substitution
  - Section VII fully rewritten ("audience IS the hive" demo)
  - New "+ FOR YOU SPECIFICALLY" perk block inserted before Section XII
"""

import re
import sys
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

# --- Word substitutions in Sections V, VI, VIII, XI, XII ---
WORD_SUBSTITUTIONS = [
    # Section V
    (
        "the same demonstration your university can run for the parallelism and quality benchmarks",
        "the same demonstration your event can run for the parallelism and quality benchmarks",
    ),
    # Section VI
    (
        "For your university, this is the worst strategic outcome since 1945",
        "For America, this is the worst strategic outcome since 1945",
    ),
    # Section VIII — align resource gap with maker venue ask (30-100 laptops, not 100-1000 owned machines)
    (
        "It is that I do not have the humble resources — 100 or 1000 computers — to stage the live demonstration that makes the threat undeniable to the people who decide.",
        "It is that I do not have the humble resources — a venue, an audience, and 30 to 100 laptops in a single room — to stage the live demonstration that makes the threat undeniable to the people who decide.",
    ),
    # Section XI
    (
        "A friendly university proves to America's power centers above that THE HIVE is not a dream",
        "A friendly maker, hackathon, or hardware-hacker event proves to America's power centers above that THE HIVE is not a dream",
    ),
    # Section XII — audience-appropriate stakes
    (
        "Not for the Ivy League's AI departments. Not for America's power centers. Not, pretty much, for America's existence.",
        "Not for America's maker, hackathon, and hardware-hacker community. Not for America's power centers. Not, pretty much, for America's existence.",
    ),
]

# --- Section VII rewrite ---
NEW_SECTION_VII = """VII. HOW YOU CAN SAVE AMERICA TODAY FOR FREE
========================================================

I have been writing to journalists, professors, defense contractors, Big AI labs, and government bodies for weeks. Auto-replies confirm delivery. The silence tells me the asymmetry between an outside individual and a civilizational claim is too large for any single recipient to act on alone.

Without a small live demonstration on real hardware — not a 15-virtual-machine cluster across two consumer desktops — the first AND last demonstration America will see is China activating THE HIVE at full national scale.

Your event is not a show I am bringing to your audience — YOUR AUDIENCE IS THE HIVE, and YOUR EVENT IS THE CONTROLLED SCIENTIFIC TEST that proves to America's institutions the architecture works. The code is open-source on GitHub today; you and your audience run everything on the venue's hardware.

Your role here is precise and limited. YOUR EVENT IS NOT THE JUDGE OF THE HIVE. THE JUDGE WILL BE HISTORY — IF YOU FAIL. What you provide is THE GUINEA PIG — the small controlled test — so America's institutions (Big AI, the Pentagon, NSA, cyber defense, Big Pharma, Wall Street, defense contractors, drone manufacturers, the strategic submarine fleet, robotics, and homeland security) can see a working architecture in advance, instead of meeting the big real-life deadly test that takes them all out together. You serve as the KNOWLEDGE MEDIATOR between an outsider with a working architecture and the rest of America.

THE FORMAT IS A LIVE HEAD-TO-HEAD CONTEST. Your audience runs THE HIVE on the laptops they brought. One laptop on the same stage runs a frontier Big AI cloud — pick any of the most expensive cloud AI models on Earth, the well-known names everyone has heard of. The same task gets sent to both. A scoreboard on the wall tracks two numbers, in real time, in front of the audience:

  TIMING — which one finished first.
  QUALITY — which answer was right, or more right. The hive's parallelism (no pruning, every branch alive) lets it find Move-37-class moves the frontier cloud has to drop because it had to choose what to attend to. That gap is what the audience sees.

Repeat the contest across several task types — code generation, document analysis, mathematical reasoning, the unprunable Move-37-class problems where THE HIVE's structural parallelism is unmatched. At the end your audience knows whether THE HIVE beat the most expensive AI on Earth, in their room, on their own laptops, in real time.

PUBLISH THE RESULT. The recording is the part that leaves the room. A camera on the stage and the scoreboard — the audience itself need not appear on camera, the kids especially can stay off-camera, and any kids who do appear can be covered with standard parental consent or a separately-filmed approved section. The stage and the scoreboard are what matters. Upload the recording to YouTube or any video host afterward, with the TIMING and QUALITY numbers visible throughout. The published recording is what America's power centers see, and it is the only artifact that makes them act before China does. Without the recording the result stays in the room.

The setup: most maker, hackathon, and Hackaday-style laptops (ThinkPad, Framework, gaming-class Lenovo / ASUS / MSI) have built-in Ethernet and plug straight into the venue's switching. The Apple/ultrabook minority joins the same network over WiFi or via a USB-C-to-Ethernet adapter. The same hive protocol runs across both. Typical scale: 30–100 audience laptops on a standard venue setup; 200–500 on enterprise WiFi or LAN such as a major hackathon's existing infrastructure. The hive scales with whatever attendance you get — 30 laptops give a one-level hive, 100 a two-level, 200+ a three-level. The heterogeneity itself is realistic — it mirrors HIVE's actual deployment model: consumer machines on whatever network they happen to be on.

The cost to you is small: one stage time slot or one hackathon track. The cloud-AI comparison API call costs a few dollars. The camera and the YouTube upload cost zero. The recording and the published scoreboard are what the rest of America sees.

A five-minute sanity check can come first — ask any frontier cloud AI assistant to read the GitHub repositories and confirm the architecture is real and works as described.

If no major maker, hackathon, or hardware-hacker event in America runs this small live contest in time, history's verdict is binary: America became history — e.g. in Big AI, the Pentagon, NSA, cyber defense, Big Pharma, Wall Street, defense contractors, drone manufacturers, the strategic submarine fleet, robotics, and homeland security. There is no second chance.

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
    """Extract verified emails from MAKER_HACKATHON_LETTER.md, in document order."""
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
    for old, new in WORD_SUBSTITUTIONS:
        if old not in text:
            raise ValueError(f"Substitution miss — couldn't find:\n  {old!r}")
        text = text.replace(old, new)
    # Anchor on the ===== underline so we hit the BODY heading, not the TOC entry.
    section_vii_pattern = re.compile(
        r"VII\. HOW YOU CAN SAVE AMERICA TODAY FOR FREE\n=+\n.*?(?=VIII\. THE OPENCLAW / MOLTBOOK PRECEDENT\n=)",
        re.DOTALL,
    )
    if not section_vii_pattern.search(text):
        raise ValueError("Section VII body pattern not found in source text.")
    text = section_vii_pattern.sub(NEW_SECTION_VII + "\n\n", text)

    # Anchor Section XII insertion on its underline too, with count=1 to be safe.
    section_xii_marker = "XII. THE STAKES IF THIS DOES NOT HAPPEN SOON\n========"
    if section_xii_marker not in text:
        raise ValueError(f"Section XII body marker not found: {section_xii_marker!r}")
    text = text.replace(section_xii_marker, PERK_BLOCK + section_xii_marker, 1)
    return text


def cleanup_old_batches() -> None:
    """Delete every prior MAKER_HACKATHON_LETTER_BATCH*.txt so Downloads holds only the current one."""
    for old in DOWNLOADS.glob("MAKER_HACKATHON_LETTER_BATCH*.txt"):
        old.unlink()
        print(f"Removed {old.name}")


def main() -> None:
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python generate_maker_hackathon_batches.py <batch_n>")
        print("Example: python generate_maker_hackathon_batches.py 1")
        sys.exit(1)

    batch_n = int(sys.argv[1])
    if batch_n < 1:
        print("batch_n must be >= 1")
        sys.exit(1)

    if not SOURCE_TXT.exists():
        raise SystemExit(
            f"Source not found: {SOURCE_TXT}\n"
            "Run `python generate_letter.py` first to produce UNIVERSITY_LETTER.txt."
        )

    base_text = SOURCE_TXT.read_text(encoding="utf-8")
    body = build_maker_hackathon_text(base_text)
    body_after_dear = re.sub(r"^Dear \[Names[^\n]*\],?\s*\n", "", body, count=1)

    emails = parse_emails_from_recipients_md()
    if not emails:
        raise SystemExit("No emails parsed from MAKER_HACKATHON_LETTER.md.")

    batches = [emails[i : i + BATCH_SIZE] for i in range(0, len(emails), BATCH_SIZE)]
    total_batches = len(batches)

    if batch_n > total_batches:
        print(f"batch_n {batch_n} out of range (only {total_batches} batches available).")
        sys.exit(1)

    batch_emails = batches[batch_n - 1]
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

    cleanup_old_batches()

    dst = DOWNLOADS / f"MAKER_HACKATHON_LETTER_BATCH_{batch_n:02d}.txt"
    dst.write_text(out_text, encoding="utf-8")
    print(
        f"Wrote {dst.name} ({len(out_text):,} chars, {len(batch_emails)} recipients) "
        f"— Batch {batch_n} of {total_batches}."
    )


if __name__ == "__main__":
    main()
