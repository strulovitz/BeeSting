# Kling Prompt Lessons — MANDATORY reading before writing any Kling prompt

**Written after Block 5 (2026-04-27) — lessons paid for in poor clips.**

---

## The core failure

Block 5 Kling prompts were lazy — 2-3 lines, no style description, no scene context, just "X glows, Y moves." The result was static-looking clips and one clip (S7) that did not even match the Kurzgesagt visual style because the style was never stated. This is unacceptable.

**The S7a/Ukraine exception is NOT the template.** In Block 4 S7a, Nir asked for an ultra-minimal Kling prompt ("just the flames") because the reference image was confusing and we did not want Kling to redraw the arrows. That was a crisis fix for a broken reference image. It is the EXCEPTION. Normal clips with clean reference images must have full, proper Kling prompts.

---

## What a proper Kling prompt must contain

Every Kling prompt must have ALL FOUR of these elements:

### 1. Visual style
Always state the style. Example:
> *"Kurzgesagt-style flat 2D animation."*

Never skip this. Without it, Kling may drift into a different visual style entirely — photorealism, 3D, crayon sketch, anything.

### 2. Scene context (what is in the frame)
Briefly describe the key elements visible so Kling knows what it is animating. Not a full ChatGPT Image description — just the 2-3 most important things. Example:
> *"A massive gold honeycomb pyramid labeled THE HIVE towers on the right, dwarfing a small human silhouette and the ALPHAGO server tower on the left against a deep burgundy night sky."*

### 3. Animation action (what moves)
Describe concrete movement — what glows, what falls, what grows, what flickers. Physical and specific. Example:
> *"The pyramid's honeycomb cells flicker and sparkle with warm gold light like a field of fireflies. The ALPHAGO tower's roof light pulses. Stars twinkle in the sky."*

### 4. Camera move
State the camera direction per the shot plan. Example:
> *"Camera holds on a wide low-angle hero shot, looking slightly upward at the three figures."*

---

## BAD prompt example (what Block 5 was doing)

> *"Flat 2D animation. The Hive pyramid's honeycomb cells flicker and sparkle like fireflies. The AlphaGo tower's light pulses softly. The stars in the sky twinkle."*

Problems: no style stated, no scene context, camera not mentioned.

## GOOD prompt example (what it should be)

> *"Kurzgesagt-style flat 2D animation. A massive gold honeycomb pyramid labeled THE HIVE towers on the right of the frame, dwarfing a small human figure and the dark ALPHAGO server tower on the left, all standing on a cream horizon under a deep burgundy night sky. The pyramid's hundreds of honeycomb cells flicker and sparkle with warm golden light. The ALPHAGO tower's single roof light pulses softly. Gold stars twinkle in the sky above. Camera holds wide on a low-angle hero shot, looking slightly upward at the three figures."*

---

## The rule going forward

**Minimal Kling prompts are the exception, not the standard.**

The only case for a minimal prompt is when the reference image is broken or confusing and you are afraid Kling will redraw it if given too much direction. In that case, write the minimum needed to preserve the reference image. This is a crisis mode. In normal production, write full prompts.

Nir's exact words (2026-04-27): *"You will take the shitty Kling that we have, and you will produce cool things with it."*

---

## Quick checklist before submitting any Kling prompt

- [ ] Does the prompt state "Kurzgesagt-style flat 2D animation"?
- [ ] Does the prompt describe the key elements in the frame?
- [ ] Does the prompt describe concrete animation — what moves, glows, falls, grows?
- [ ] Does the prompt include the camera move from the shot plan?
- [ ] Is the prompt longer than 3 lines? (If not, it is probably too short.)
