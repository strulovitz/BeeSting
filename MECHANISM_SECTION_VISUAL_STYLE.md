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

**Option 3 — 80s military training film / declassified briefing.** Locked by Nir 2026-04-18.

Rationale (Nir's words): *"I want you to keep all 3 options in github and push but i want to choose number 3 it is awesome."*

Applied to all Mechanism X, Y, Z, W shots. The HUD kill sequence (S07-S15) stays photoreal and is not affected by this decision. The pre-HUD sequence (S00-S06) also stays photoreal.

---

## Style bible for Option 3 (for all Mechanism shots going forward)

**Medium:** cel animation, hand-drawn-inked look. Not 3D, not photoreal, not modern flat vector.

**Palette:** muted military training film — faded army green, dusty tan, cream, dull orange, chalk white, charcoal. Think 1970s-80s Pentagon classroom projector reels. No bright saturated colors.

**Characters:** slightly stiff, simplified anatomy, limited animation frames (the kind of movement an animator on a 1980s government budget could afford). Faces are legible but not emotive — expressions are held for multiple frames.

**Backgrounds:** sparse, diagrammatic. Rooms are indicated with a few lines and a flat color. Drones, phones, bunker walls render as simple shapes with hand-inked outlines.

**Overlay treatment:** visible film grain, occasional dust specks, mild frame jitter, "CLASSIFIED" / "CONFIDENTIAL" / "TRAINING FILM" stamps in corners, a small reel-countdown number bottom-right on occasion, the general feel of a 16mm film being projected.

**Typography (when needed):** stenciled military sans-serif, monospaced typewriter type. White or cream over the image.

**Tone:** the narrator is a quietly competent briefer walking trainees through the material. Absolutely no wink at the camera. The visuals are slightly dated and slightly slow — but they are NEVER comedic on purpose. The irony is the audience's to find.

**What to avoid:** anime faces (too contemporary), comic-book halftone (wrong era), Kurzgesagt flat-vector (too modern), modern 3D, speech bubbles, memes, emojis in the shots themselves.

---

## How to apply this to Kling prompts (Mechanism shots)

Every Kling prompt for a Mechanism X/Y/Z/W shot should open with something like:

> *"1980s military training film cel-animation aesthetic — muted faded palette (army green, dusty tan, cream), simplified hand-inked characters, sparse diagrammatic backgrounds, visible film grain, occasional CLASSIFIED corner stamp. [then describe the specific action]."*

Every reference image prompt for ChatGPT Image 1.5 should open with the same style-bible intro.

---

## Relationship to prior docs

- `PART_1_WAR_BRIEF.md` shot list (the old plan where Mechanism X was 8 photoreal shots) is SUPERSEDED for the Mechanism section specifically.
- `HOLY_TEXT.md` Blocks 7-10 (the four mechanism narrations) are unaffected — only the visuals change.
- `HANDOFF_VIDEO_PRODUCTION.md` Lessons 1-20 still apply (including Lesson 17 "do not describe subjects as moving" and Lesson 20 "every Kling prompt needs camera motion").
