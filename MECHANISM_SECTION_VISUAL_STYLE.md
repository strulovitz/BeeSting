# Mechanism Section Visual Style (Blocks 7-10) — locked 2026-04-18

Decision date: 2026-04-18.
Scope: Mechanism X, Y, Z, W visual shots (the post-pause teaching/explainer section).
HUD kill sequence (S07-S15) and pre-pause shots keep their existing photorealistic look — this style only applies to the explanatory Mechanism section where the narrator is actively teaching the viewer.

---

## Why we needed a different style for the Mechanism section

The pre-pause section is CATASTROPHE cinema — bunker attack, fireball, thermal hunt, target locked. Photoreal, serious, emotional. The Mechanism section is TEACHING — the narrator is explaining WHY the hive works, using analogies (video call → voice → SMS, drone, queen, workers). Photoreal shots of 8 near-static scenes for ~12 seconds each would kill attention by boredom ("we don't need the drones to kill them, we kill them with boredom" — Nir 2026-04-18).

We needed a visual style that:
- Keeps the teaching energy alive (more than a static photo can)
- Does NOT undercut the gravitas of the larger video
- Reads as "documentary / serious explainer," not as comedy or kids' content
- Is consistent across all 4 mechanisms (X, Y, Z, W) so the viewer knows the teaching frame

---

## The three options considered

### Option 1 — Kurzgesagt / Vox-style flat 2D motion graphics
Clean flat-vector shapes, limited duotone palette (teal + orange, or similar), smooth educational animation. Very contemporary, polished, "serious YouTube explainer" aesthetic. Gold standard for "serious topic, watchable animation." Risk: can feel over-designed or too corporate for the BeeSting voice.

### Option 2 — RSA Animate whiteboard
Hand-drawn illustrations appearing live on a white or black background as the narrator speaks. Quirky stick figures and diagrams, lo-fi charm, obviously educational. Risk: too informal for the weight of the content; might read as TED-talk-y.

### Option 3 — 80s military training film / declassified briefing (CHOSEN)
Cel-animated limited palette (muted tans, faded greens, dusty browns), slightly dated character designs, film grain, occasional frame jitter or cigarette burn, "CLASSIFIED" or "DECLASSIFIED 1987" corner stamps, narrator-of-authority vibe. The vintage look IS the irony — we are in a serious briefing from an alternate timeline where this tech was declassified. The retro aesthetic reinforces "this is a briefing, pay attention," and the dated character animation keeps the eye interested without undermining gravitas.

---

## The choice

**Option 1 — Kurzgesagt / Vox-style flat 2D motion graphics.** Locked by Nir 2026-04-18.

Rationale (Nir's words, after briefly choosing Option 3 and reconsidering): *"after smiling for a few seconds it just looks lame. i want number 1 please. what you called the golden standard."*

Option 3 (80s military training film) was rejected because even though it is visually striking for the first few seconds, the worn-film retro vibe has a shallow laugh curve — after the ironic smile it just reads as "old and lame" and loses energy across a 95-second teaching segment. Option 1 scales better across four full mechanisms because it is built to be SUSTAINED educational viewing (the entire Kurzgesagt / Vox / TED-Ed category is proof of concept).

Applied to all Mechanism X, Y, Z, W shots. The HUD kill sequence (S07-S15) stays photoreal and is not affected by this decision. The pre-HUD sequence (S00-S06) also stays photoreal.

---

## Style bible for Option 1 (for all Mechanism shots going forward)

**Medium:** flat 2D vector motion graphics, clean and polished. Think Kurzgesagt-style, Vox Explained, TED-Ed, Polygon's "Explained in 5 minutes." Not photoreal, not 3D, not cel animation, not hand-drawn.

**Palette:** duotone or triotone, bold and confident. Suggested core palette for BeeSting: deep navy or charcoal background, warm amber/orange highlight color, soft cream or white for the accents. (Keep the SAME palette across all 4 mechanisms so the Mechanism section reads as one unified teaching segment, visually distinct from the photoreal sections on either side.) Avoid muddy tones. No gradients inside shapes — flat fills only, occasional subtle background gradient is fine.

**Characters:** simplified geometric bodies, round heads, no facial features beyond eyes (sometimes a mouth). Expressive through POSE and GESTURE, not facial detail. Limbs are simple cylinders or rectangles. Proportions are slightly stylized (larger heads, shorter bodies) so characters read at any size.

**Objects and props:** flat vector with clean bold outlines, simplified geometric forms. Phones, drones, bunker walls are iconic shapes — immediately recognizable silhouettes, never fussy detail. A drone is a square body with four circles for propellers and a small antenna line, not a rendering of a specific model.

**Backgrounds:** flat color or simple two-band gradient. Environments indicated with minimal elements (a single horizon line, a stylized building outline, a few abstract shapes). Never photo-realistic backgrounds under the vector characters.

**Motion:** smooth, confident, easing in and out. Objects slide/pop/bounce into frame rather than fade. Text labels snap into place. Diagrams build element by element. Camera moves are simple (straight push-in, straight pan) — no handheld shake.

**Typography:** modern geometric sans-serif (think Kurzgesagt's "Andada" or Helvetica-adjacent). Used sparingly for labels and key concepts. Bold weights.

**Tone:** confident, warm, educational. The narrator is explaining something fascinating to a smart friend — not lecturing, not performing. The visuals trust the viewer to follow.

**What to avoid:** 3D rendering, photo-realistic textures, hand-drawn sketchiness, cel-animation line wobble, retro film grain, halftone comic dots, speech bubbles, emojis in the shots themselves, cluttered backgrounds, busy color palettes.

---

## How to apply this to Kling prompts (Mechanism shots)

Every Kling prompt for a Mechanism X/Y/Z/W shot should open with something like:

> *"Kurzgesagt-style flat 2D motion-graphics animation — simplified geometric characters, bold duotone palette (deep navy background + warm amber highlight + cream accents), clean flat vector shapes, smooth confident motion, no gradients inside shapes, no photo-realism. [then describe the specific action]."*

Every reference image prompt for ChatGPT Image 1.5 should open with the same style-bible intro.

---

## Three engagement tricks ON TOP OF the style (locked 2026-04-18)

The Kurzgesagt visual style is necessary but not sufficient to hold attention across a 95-second Mechanism X segment. INSIDE the style, every shot in the Mechanism section must also obey these three tricks — requested verbatim by Nir 2026-04-18:

### Trick 1 — Split each ~12-second "shot" into 2× ~6-second clips
Instead of 8 long 12-second shots for Mechanism X, generate 16 short ~6-second clips. Kling 3.0 Omni is more reliable on shorter clips (Handoff Lesson 2: "If narration is 12+ seconds, split into two ElevenLabs recordings and two video clips. Kling is more reliable on shorter clips"). Shorter clips also give the editor more cut points in Premiere, which is essential for pacing a teaching section.

### Trick 2 — Every clip is a MICRO-BEAT (start → happen → land)
A clip is NEVER just one static pose. Each clip has a tiny three-step micro-story:
- **Start** — something enters the frame, or the character is in a ready position
- **Happen** — something changes, moves, glitches, gets sent, arrives, fails, succeeds
- **Land** — the consequence clicks into place (a reaction, a label appears, the symbol snaps into its final position)

Even a 6-second clip can hold a visible start → happen → land arc if the motion is confident (Kurzgesagt's whole aesthetic is built on this). A static character holding a phone for 6 seconds is wasted credits; a character who raises the phone, watches it glitch, and winces is alive.

### Trick 3 — Mix angle changes across consecutive clips (wide → close, or side → POV)
Across the 16 clips of one mechanism, consecutive clips SHOULD NOT share the same composition. Alternate deliberately:
- Wide establishing → tight close-up of the same subject
- Side profile → over-the-shoulder POV
- Character-centered → object-centered (phone, drone, network diagram)
- Flat icon view → isometric-angled view

This mimics how real explainer videos on Kurzgesagt / Vox / TED-Ed keep the eye moving without the underlying scene changing. Same scene, different angle on each clip = alive. Same scene, same angle = frozen and boring.

### Applying all three tricks to a shot prompt

Every Kling prompt for a Mechanism shot should:
1. Name the Kurzgesagt style (opening line of the prompt as above)
2. Name ONE specific camera framing for this specific clip (wide / close / side / POV / top-down)
3. Describe the MICRO-BEAT as three steps in one sentence (e.g., *"character starts holding the phone flat, the screen pixelates and freezes, the character winces and leans back"*)
4. NAME consistent palette items (navy + amber + cream) so clips stitch visually across all 16

If a prompt is generating a still reference image (ChatGPT Image 1.5), skip trick 2 (micro-beats are for motion) and focus on a single SNAPSHOT from the middle of the micro-beat — typically the "happen" moment, which is the most visually interesting frame.

---

## Rejected options (for the record)

### Option 2 — RSA Animate whiteboard
Lo-fi hand-drawn illustrations appearing live on a white or black background. Rejected because it reads as TED-talk-y and too informal for the catastrophe-weight frame of BeeSting.

### Option 3 — 80s military training film / declassified briefing
Cel animation with muted retro palette, film grain, CLASSIFIED corner stamps. Rejected after brief selection because the retro vibe reads as "lame" after the first few seconds of irony — it does not sustain across a 95-second teaching segment.

---

## Relationship to prior docs

- `PART_1_WAR_BRIEF.md` shot list (the old plan where Mechanism X was 8 photoreal shots) is SUPERSEDED for the Mechanism section specifically.
- `HOLY_TEXT.md` Blocks 7-10 (the four mechanism narrations) are unaffected — only the visuals change.
- `HANDOFF_VIDEO_PRODUCTION.md` Lessons 1-20 still apply (including Lesson 17 "do not describe subjects as moving" and Lesson 20 "every Kling prompt needs camera motion").
