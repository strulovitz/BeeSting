# MIT Letter — Table-of-Contents Plan (the "trick")

**Status:** Planned, NOT yet applied to MIT_LETTER.md. Saved 2026-05-03 before Nir went to the supermarket so the idea isn't lost.

---

## The trick

Add a **Table of Contents** at the top of the letter, right after one bold opening sentence. Reader sees in 5 seconds that the letter has structure, picks their entry point, jumps to the section that interests them.

---

## Why it works (the load-bearing reasons)

1. **Solves the scroll problem.** The single biggest barrier to a busy academic reading the letter is the sheer length. A TOC kills that barrier in one move — they see the structure in seconds and know where the substance lives.

2. **Itself a credibility signal.** Crackpot mail famously does NOT have organized structure. A clean TOC at the top signals "this person organized their thinking" before the reader has read any actual content.

3. **Each TOC entry is its own hook.** "How it breaks MAD" / "10 ways America falls" / "Why this falls to you" — each entry is a mini subject line. A reader scanning the TOC gets 6+ chances to be hooked, instead of just one chance from the opening sentence.

4. **Lets the reader pick their entry point.** A geopolitics person clicks "MAD-breaking." An AI researcher clicks "alignment proof." A skeptic clicks "verify everything." Each reader picks the door that's most interesting to them — vastly more likely to get read than linear text.

5. **Defends against the dismissal sequence.** When the letter has clear structure, the reader can't dismiss after 2 sentences — they're forced to scan the TOC, see the substance is real, and decide whether to engage with at least one section.

---

## Where it goes

```
[Subject line — already locked]
Dear [Names],

[ONE bold opening sentence — energetic, matches subject]

[TABLE OF CONTENTS — 5-7 entries, each a hook]

[Body sections in their existing order]
```

The bold opening sentence still grabs them. The TOC then says "here's what's inside, pick a door."

---

## Anchor links

- HTML email supports `<a href="#section">` style anchor links — works in Gmail, Outlook, Apple Mail (the major academic email clients).
- For plain-text or stripped HTML clients, the TOC degrades gracefully into a numbered visual outline.
- Worst case = visual outline, best case = clickable nav. Either way it works.

---

## Suggested 5–7 TOC entries (group the existing 13 sections)

Rough mapping — to be refined:

1. **What the architecture is** (1 sentence + plain-English description)
2. **How it solves alignment** (the architectural-constraint argument)
3. **The 10 ways America falls** (the 11 numbered industry-collapse bullets)
4. **How it breaks MAD** (the underwater-drone-swarm second-strike kill)
5. **Why this falls to you** (the OpenClaw precedent + Chinese-embassy logical-next-step + preferred path)
6. **Verify everything** (links to GitHub repos, MadHoney book, BeeSting videos)

Could expand to 7 by separating "preferred path" and "OpenClaw precedent" into distinct entries if needed.

---

## Open questions to resolve when we come back to this

- Should the TOC use bold/italic/heading styles, or plain numbered list?
- Anchor link target names — match section headers exactly or use shorter slug?
- Should the TOC come BEFORE or AFTER the bold opening sentence? (Current plan: AFTER one bold sentence, BEFORE the body.)
- Final wording of each TOC entry — each one is a mini-hook so it deserves the same care as the subject line.
- Whether to keep the existing top-of-letter "Status / Subject / Section order" admin section or move it to a separate doc.

---

## Decision rule

When we come back to this, the criterion for each TOC entry is:
- **Does this entry make the reader want to click/scroll to that section?**
- **Does it accurately describe what's there, or is it bait?** (Must be honest — bait gets dismissed.)
- **Is it short enough to read in 1 second?**

---

*Saved by Opus 4.7 at Nir's request, 2026-05-03, before any application to the live letter.*
