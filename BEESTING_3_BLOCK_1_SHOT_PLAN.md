# BeeSting Episode 3 — Block 1 Shot Plan
## Opening minute: equation hook + pharmacy collapse + 5 nightmares

---

## Status as of 2026-04-30

- **Plan author:** Opus 4.7 (planning session, 2026-04-30).
- **Total runtime:** ~57 seconds.
- **Sections:** 6 (1 equation slide + 1 silent opener + 5 paired nightmares).
- **Narration audio:** 1 of 6 recorded (`E03-block01-01-equation-slide.mp3`, 16 seconds, Kristen). 5 still to record.
- **Visuals:** 1 of 6 produced (`E03-opening-A-medicine-cabinet-avalanche.mp4`, the cabinet flood). 5 still to produce.

---

## Block at a glance

- **Audience:** Big Pharma CEO (the decision-maker who must read this), via the secretary who clicks FORWARD (the gatekeeper who must be hooked enough to forward).
- **Tone:** cold transactional. Monkey-wrench register, NOT moral outrage. The narrator is a controlled news anchor who has already decided what is going to happen and is calmly informing the executive.
- **Visual style:** photorealistic horror-thriller film stills. Each clip a moment that could be a frame from a contemporary thriller. No flat 2D motion graphics in Block 1 (Block 2+ may use them for the chapter teasers).
- **Argument arc:** the equation summary names four threats; the silent opener visualizes the industry's collapse (every wall falling at once); each of the 5 nightmares zooms into one specific patient/ executive consequence. Cause → effect → effect → effect → effect → effect.

---

## Production rules — LOCKED, do not change without explicit Nir approval

These rules accumulate the lessons from BeeSting 1 and BeeSting 2 production, plus lessons specific to Episode 3.

1. **Kling settings:** model = Kling 3.0, resolution = **Pro** for the opener / 720p for cheap variants if needed (decision per clip), Native Audio = **OFF** always, mode = **reference image**, aspect ratio = **16:9**.
2. **Never restrict movement in Kling prompts.** No "minimal," "subtle," "no movement." Describe the scene, let Kling decide. (See `feedback_kling_no_movement_restriction.md` in claude-memory.)
3. **Reference images come from a prototype + meta-reference workflow.** For any visual with a human character, generate a text-only prototype in ChatGPT Image 1.5 first, then attach that prototype PNG as a reference inside ChatGPT Image when generating each scene image. Saying "same woman as before" in pure text does not work — both Kling and ChatGPT Image are stateless. (See `feedback_kling_scene_multiple_refs.md`.)
4. **Allowed text in visuals:** NSA, BIG AI, BIG PHARMA, PRIVATE MODE, TOP SECRET. Short brand-style labels only. No technical diagrams, no labeled arrows, no flowing text. Text in the reference image is drawn-in and frozen — Kling does not animate text.
5. **Never name real Big Pharma companies in visuals.** Allowed text ends at "BIG PHARMA." Specific company names from the script's blacklist must not appear on signage, packaging, screens, or anywhere visible in any frame.
6. **Pharmaceutical packaging must be heterogeneous when visualizing the cascade.** Variety = different drugs for different body parts = the cascade message. One repeating bottle reads as addiction. Use orange amber prescription bottles, white pill bottles, foil blister packs, pen injectors, eye drops, glass vials, asthma inhalers, foil tablet strips, cardboard boxes, adhesive patches, squeeze tubes — all mixed.
7. **Female-pronoun audio pairs with female-coded visuals.** Nightmare audios 1, 2, 3, 4 use "she/her"; the corresponding visuals show female patients. Nightmare 5 is gender-neutral and pairs with the cemetery (no specific gender shown).
8. **Same voice + same settings across the entire episode.** Kristen — Authoritative E-Learning Expert. Settings: speed 111, stability 30, similarity boost 75, style 75, m2, speaker boost on.
9. **Verify audio durations with Nir, do not estimate them by word count.** The equation slide narration was assumed ~6-7 seconds and turned out to be 16 seconds. Always ask Nir for the actual duration after a take is generated.
10. **Push to GitHub after every meaningful edit.** Each prompt, each rendered file, each plan revision gets committed and pushed immediately. Do not batch.
11. **Do not delete Nir's files.** Including renaming-via-mv when there is any ambiguity. Use cp + clean name for backups; leave the original in Downloads for Premiere relinking.
12. **Drag every new mp3/mp4 into Premiere immediately** when it lands in Downloads.
13. **One clip at a time.** Write reference image prompt → generate PNG → verify with Nir → write Kling prompt → generate MP4 → save → continue.

---

## Section 0 — Equation slide (~6 seconds visible, ~7 sec audio)

**Narration line covered:** *"This revolutionary Israeli software, running for free in every American kitchen and every Chinese laboratory, will collapse Big Pharma tomorrow.* (start of the line)

**Visual:** the BeeSting equation icons in the series style. (Specific design TBD — needs the same family treatment as Episode 1 and 2's equation slides.) Likely 🇨🇳💪 ➕ 🇮🇱🧠 ➡️ 🇺🇸 + a Big-Pharma-coded skull or pill icon, in the same flat-icon family. Final visual not yet designed.

**Status:** PENDING — Nir has not yet specified the exact equation icons for Episode 3. Visual reference image to be designed when Nir confirms the icon set.

**Animation:** static or near-static — same as BeeSting 1 and 2's equation slides hold for several seconds.

---

## Section 1 — Pharmacy collapse (silent under equation audio finish, ~10 seconds total, three Kling clips)

**Narration line covered:** *"...Your prices, your patents, your hidden side effects, your dead patients — every wall will fall at once."* (continuation of equation slide audio, plays over this section silently)

**Concept:** A pharmacy storefront in a city street at night. A green neon sign reading "BIG PHARMA" replaces where "PHARMACY" would normally be. Flanking the BIG PHARMA text: green pharmacy cross on the left in bright neon, caduceus (winged staff with two entwined snakes) on the right in bright neon. Above the main sign, a horizontal row of four smaller neon icons each in its own color, each representing one of the four threats named in the audio:

- Light-green dollar sign (prices)
- Gold padlock (patents)
- Red warning triangle with exclamation mark (hidden side effects)
- White skull and crossbones (dead patients)

The sign assembly glows against a dark, deserted city street. Slight ground fog, wet sidewalk reflecting the neons. Camera position: across the street, slightly low angle looking up at the storefront so the sign and icons fill the upper-middle of the frame.

**Three Kling clips, cut together in Premiere:**

### Section 1, Clip A — Storefront calm (4 seconds)

**Reference image (Reference 1, prototype):** the pharmacy storefront in calm normal state — sign and four icons all glowing peacefully. This is the ground-truth image of the location. Generated text-only in ChatGPT Image 1.5 (no attachment).

**Animation:** ambient — slight fog drift, faint flicker of neon, distant traffic implied (no visible cars, but city-night atmosphere). Camera: slow push-in or static hold from across the street.

**Mood:** calm before. The trick still working.

### Section 1, Clip B — Lightning strike (3 seconds)

**Reference image (Reference 2):** same exact pharmacy as Reference 1, same exact sign, same exact icons, same exact street — but with a massive lightning bolt striking down from the sky onto the sign. Generated in ChatGPT Image 1.5 with **Reference 1 ATTACHED** as meta-reference, so the storefront looks identical between the two images.

**Animation:** lightning bolt comes down from sky, strikes the BIG PHARMA sign. Single motion. No explosion yet — the lightning is the strike, the explosion is Clip C.

**Camera:** held wide, slight shake on impact.

**Mood:** the impact moment.

### Section 1, Clip C — Explosion (3 seconds)

**Reference image (Reference 3):** same exact pharmacy as Reference 1 — but mid-explosion: all four neon icons bursting in showers of sparks, the BIG PHARMA sign exploding, the pharmacy's glass storefront blowing outward, glass shards in mid-air, debris, smoke. Generated with **Reference 1 ATTACHED** as meta-reference.

**Animation:** full explosion outward — sign bursting, glass shattering, sparks and shards flying toward the camera, smoke billowing. Single motion.

**Camera:** held wide, possibly slight pull-back as debris approaches.

**Mood:** every wall falling at once — visual payoff to the audio's closing line.

**Status:** PROMPTS NOT YET WRITTEN. Three pending questions for Nir before prompts: confirmed (a) camera angle = across-street slightly-low, (b) empty deserted street, (c) slight ground fog + wet sidewalk reflecting neons. Nir is currently confirming these.

---

## Section 2 — Medicine Cabinet Avalanche (10 seconds)

**Narration line covered:** *"Your patient's medicine cabinet. Every bottle inside is your revenue. Now, for free, in her kitchen, in plain English — she has the map of which of your pills is killing her. She stops swallowing. Every Big Pharma company is about to become the next Purdue."*

**Concept:** A 38-year-old white American suburban woman in pale-blue cotton pajamas (long-sleeve button-up + matching pants) opens her bathroom medicine cabinet. An avalanche of mixed pharmaceutical packaging pours out — orange amber prescription bottles, white pill bottles, foil blister packs, capsules — flooding the bathroom around her until she is buried chest-deep in the flood.

**Reference image workflow:**
- Prototype: full-body portrait of the woman in pajamas against neutral cream-bathroom-tile background. Locks her face, hair, clothing, recognizable details (hazel-green eyes, beauty mole below left ear, freckle at right corner of mouth, chestnut wavy hair).
- Scene 1 (normal morning): same woman in her bathroom, cabinet still closed, sleepy, reaching toward the cabinet handle.
- Scene 2 (first pills): same woman, cabinet just swung open, first pills tipping out, her face cracking from sleepy to confused.
- Scene 3 (buried): same woman, chest-deep in a flood of mixed pharmaceutical packaging, hollow expression, cabinet still vomiting pills behind her.

**Kling clip:** 10-second tidal-wave avalanche of pills pouring from the medicine cabinet, drowning the bathroom, burying the woman. Camera slowly pushes in from medium three-quarter to close-up on her hollow face.

**Status:** RENDERED. All three scene PNGs and the 10-second Kling clip are complete:
- `E03-opening-A-prototype.png`
- `E03-opening-A-scene1-normal-morning.png`
- `E03-opening-A-scene2-first-pills.png`
- `E03-opening-A-scene3-buried.png`
- `E03-opening-A-medicine-cabinet-avalanche.mp4`

Audio (Nightmare 1 narration with Kristen) NOT YET RECORDED. The narration text is in `E03-block01-opening-narration.txt` and in `elevenlabs_prompt.txt` (the active paste-ready file).

---

## Section 3 — Family Dinner Subtraction (10 seconds)

**Narration line covered:** *"Her family dinner. The chair where her father sat — your painkiller, the next Vioxx. The chair where her brother sat — your antidepressant, the next Vioxx. The chair where her mother sat — your heartburn pill, the next Vioxx. Every blockbuster you sell is about to become one."*

**Concept (high-level, NOT YET DETAILED):** Suburban dinner table, four place settings, warm evening light, plates of food. One chair empties (father). Then another (brother). Then another (mother). By the end of the shot, only she remains at the table; the food on the empty plates is still steaming. The visual enacts the deaths in sequence as the audio names each drug class.

**Reference image workflow:** TBD. A "family establishing prototype" showing all four family members at the table, then 3 scene images showing the chair-emptying progression. Multiple human characters — needs careful prototype design.

**Kling clip:** 10-second sequence of three chairs emptying in sequence. Likely needs to be assembled from multiple Kling clips OR rendered as one clip with carefully timed motion.

**Status:** NOT STARTED. Audio text locked. Visual concept not yet planned in detail. Reference images and Kling prompts not yet written.

---

## Section 4 — Insurance Letter (10 seconds)

**Narration line covered:** *"The denial letter your insurance partner just mailed her. She walks away from your pharmacy. She buys the same drug from Mumbai for the price of a coffee. Your pricing power was a wall made of paper."*

**Concept (high-level, NOT YET DETAILED):** A woman at her kitchen table opens a white envelope. Camera pushes in on the letter — the words "Coverage Denied" bloom into focus (this would be "BIG PHARMA"-style allowed text, simple block letters, drawn into the reference image). She rises, walks out of frame. A pharmacy storefront aisle empty as she walks past (or alternatively, a Mumbai pharmacy with a tiny price tag visible).

**Reference image workflow:** TBD. Likely the same woman as Section 2 (or a different one — TBD). 1 prototype + 2 or 3 scene images.

**Kling clip:** 10-second sequence — open letter → walk away → pass empty pharmacy. May need to be split into 2 Kling clips.

**Status:** NOT STARTED.

---

## Section 5 — Body Price Tags (10 seconds)

**Narration line covered:** *"Her body — the way McKinsey priced it on a slide for you. Liver. Hip. Memory. Overdose. Every billing code is walking out of your balance sheet — because the same molecules in your pipeline are being patented in Shanghai before you can file in Washington."*

**Concept (high-level, NOT YET DETAILED):** A woman walks down a suburban hallway in pajamas. Floating price tags appear, attached by red strings to parts of her body — different organ areas, different prices. She doesn't see them. She just keeps walking. McKinsey's slide-deck unit-economics made literal.

**Reference image workflow:** TBD. 1 prototype + 2-3 scene images (price tags appearing progressively).

**Kling clip:** 10-second walk with price tags appearing one by one or all at once.

**Status:** NOT STARTED.

---

## Section 6 — American Cemetery (10 seconds)

**Narration line covered:** *"The American graveyard. More dead Americans than every war since Vietnam — every one of them prescribed by you. The dossier on every grave now sits in every angry patient's kitchen. One patient already shot a healthcare CEO. The next stone here is yours."*

**Concept (high-level, NOT YET DETAILED):** Aerial shot of a suburban American cemetery at dawn. Camera pulls back. The headstones don't end. They keep going past the horizon. (Stretch goal: years and numbers etched on each headstone — "1999 — 10,000," "2007 — 35,000," "2021 — 80,411" — but text on every headstone is risky for Kling. Likely instead: each headstone is just a normal headstone, the SCALE is the message.)

**Reference image workflow:** Likely a single establishing reference image of a cemetery from above, then a Kling clip with the camera pull-back motion. Possibly 1 prototype + 1 scene image. No human character — easier than the patient-based visuals.

**Kling clip:** 10-second aerial pull-back over endless headstones at dawn. One clean motion.

**Status:** NOT STARTED.

---

## Order of operations from here

1. Resolve Nir's three pending answers for Section 1 (camera angle, empty/alive street, weather).
2. Write the three reference image prompts and three Kling prompts for Section 1 (pharmacy collapse).
3. Generate Reference 1 → verify → generate References 2 and 3 with attach → verify → render the three Kling clips.
4. Record audio for Sections 2–6 (Nightmares 1 through 5) using Kristen, paste-ready text already in `elevenlabs_prompt.txt`/`E03-block01-opening-narration.txt`. Expect actual durations to differ from estimates — verify each one with Nir.
5. Plan and produce visuals for Sections 3, 4, 5, 6 (one section at a time, one clip at a time).
6. Design the equation slide visual (Section 0).
7. Assemble Block 1 in Premiere.
8. Move to Block 2 (chapter-4 teaser sweep).
