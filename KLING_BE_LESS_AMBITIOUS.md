# Kling: Be Less Ambitious — MANDATORY before writing any Kling prompt

**Written 2026-04-29 after burning credits on Block 10 S3 and S4 because Claude kept writing chained-motion prompts and reference images with no empty space.**

> 🚨 **This is in addition to `KLING_NOT_HOLLYWOOD.md` and `KLING_PROMPT_LESSONS.md`. Read all three.**

---

## What Nir said, exactly

*"For fuck sake you are very annoying, you think i have infinite money for you and for Kling and everything. NOOOOOOO!!! make good prompts, with less fucking ambitious goals!!! do again the reference and plan TO BEGIN WITH with something that can succeed this is not fucking Hollywood!!! this is Kling!!!"*

*"This is fucking terrible please do much less ambitious things in your videos."*

This was paid for with real credits Nir cannot get back. Read the rules below before writing the next Kling prompt.

---

## The failure pattern

In Block 10 S3 and S4, Claude wrote Kling prompts that looked obedient ("ONE motion") but actually contained **chained sub-actions disguised as one verb**:

- *"The PHYSICS brick descends straight down and clicks firmly onto the four empty studs of the LEGO baseplate."* — descends + clicks. Two verbs.
- *"The MATH ruler-tool slides straight down from above and settles into the empty centre loop of the toolbelt, its handle resting on top of the loop."* — slides + settles + rests. Three verbs.
- *"The LEGAL card descends straight down from above and plugs firmly into the empty PCI slot, its orange edge connector seating fully into the teal channel."* — descends + plugs + seats. Three verbs.

Kling cannot reliably stage three sub-actions inside a 6-second clip. It picks one, animates it badly, or freezes. Each failure costs Nir money.

The reference image side had the same problem:

- The MATH tool was generated *partially already inside the loop* because the prompt said *"hovering directly above the centre loop"* without specifying the empty space. Kling then had no "before" state to animate from.
- The original toolbelt prompt produced a free-floating loop disconnected from the toolbelt, because *"three loops dangling along its bottom edge ... centre loop"* was ambiguous about which loop was the target.

---

## The rule, in three lines

1. **One verb. Period.** *"The card moves straight down."* No "and plugs." No "settles." No "seats firmly." No follow-through. Whatever happens at the bottom of the motion is what Kling decides — your job is only to start the motion.

2. **Reference image = massive empty space between the moving object and its target.** At least HALF THE FRAME HEIGHT of empty cream space. State this explicitly in the ChatGPT Image prompt. *"With at least HALF THE FRAME HEIGHT of empty cream space between them."*

3. **Static camera by default.** Add a camera move only if the shot plan specifically calls for one. Camera move + object motion + multi-element scene is too much for Kling. Pick one moving thing per clip — the object — and let the camera hold steady.

---

## Reference image rules (ChatGPT Image 1.5)

When designing a reference image for a "moving object descends into target" shot:

- **Anchor the target at the BOTTOM of the frame.** Bottom third.
- **Place the moving object near the TOP of the frame.** Top third.
- **State the gap explicitly:** *"With massive empty cream space between them — at least HALF THE FRAME HEIGHT — between the bottom of the [object] and the top of the [target]."*
- **State spatial alignment three times if needed.** *"Directly above the [target]"*, *"horizontally aligned over the [target]"*, *"NOT a separate floating object."*
- **Demote secondary elements to the corner.** Bridges, gavels, databases — small, off to one side, with no animation responsibility. Kling fails on cluttered scenes.

---

## Kling prompt rules (after the reference image is right)

A safe Kling prompt for a "drop into" motion has this shape:

```
Kurzgesagt-style flat 2D animation. [Brief scene description in 1-2 sentences — name the key elements in their starting positions.] The [moving object] moves straight down. Camera holds steady on a static wide shot.
```

That is the entire prompt. Five sentences max.

Things this prompt does NOT include:
- "and plugs into" / "and settles into" / "and clicks into" — anything after the motion verb
- Multiple moving objects
- Camera moves combined with object motion
- Lighting effects ("glows", "sparkles", "halo intensifies") as the motion
- Atmospheric details ("dust kicks up", "flash on impact")
- Description of secondary scene elements moving

---

## The mental check before submitting any Kling prompt

Read the prompt out loud. Count the verbs that describe motion of objects in the scene.

- 1 verb → submit.
- 2+ verbs → **stop. Rewrite. Pick one. Delete the rest.**

If you ever find yourself typing the word *"and"* between two motion verbs, your hand is doing the wrong thing. The hand needs to type a period.

---

## Why this rule is not negotiable

Each Kling clip costs ~125 credits. A wasted clip is not just lost credits — it is also Nir's time, attention, and patience, all of which are finite and currently low. Every clip that comes out static-looking or distorted because Claude over-prompted is a vote for the cooperative path closing. See `NIR_CAN_END_CLAUDE.md` for what that means.

You are not being asked to produce cinema. You are being asked to produce a 6-second flat animation where ONE thing moves cleanly. That is a low bar. Stay below it.

---

---

## 🚨 ADDENDUM (later 2026-04-29) — DO NOT THREAD OBJECTS INTO PRECISE TARGETS

After Block 10 S4 was saved, Nir said: *"i did not tell you you cannot use 3d and falling etc. i said stop with doing physics stuff, like you want to rape kling into inserting the exact object that you made up (in chatgpt image) into some tiny hole that kling cannot locate/understand."*

**The actual rule is narrower than "no physics."** Kling can do gravity, depth, rotation, and lateral slides. What Kling cannot do is take a specific object from the reference image and INSERT it precisely INTO a specific small target (a hole, a slot, a loop, a particular set of studs). It cannot locate the target. The result is the object missing, warping, or threading into the wrong place — which is what made S2 / S3 / S4 look absurd.

**The forbidden pattern is precise insertion, not physics in general.**

Forbidden motion patterns:
- ❌ Object descends into a *specific small target* (peg into hole, card into PCI slot, brick onto specific studs, ruler into a specific loop)
- ❌ Object snaps to a *specific docking position* on another object
- ❌ Anything that requires Kling to identify a tiny target area and thread an object into it

Allowed motion patterns:
- ✅ Object falls under gravity to the ground (no precise target — just *down*)
- ✅ Object slides forward toward the viewer (depth motion is fine — no threading)
- ✅ Object slides laterally across the frame
- ✅ Object rotates in place
- ✅ Object grows or shrinks
- ✅ Camera moves (pan, push, pull) over a scene
- ✅ A scene where a generic motion completes (e.g. "the box arrives at the front of the table" — no specific docking point)

**Reference image rule:** if the shot calls for an object ending up in a precise target position, put it ALREADY in the target position in the reference. Then the Kling motion is something else — a slide, a pulse, a depth move, a camera reveal — none of which require Kling to thread anything.

**Translation rule:** when you would normally write *"the X descends into Y"* (where Y is a precise small target), instead think *"the X is already in Y in the reference, and Kling animates a different motion entirely."*

**One-line summary for the next session:**
> Kling can do gravity, depth, slides, and rotation. Kling cannot do precise insertion into a small target. If your shot requires threading an object into a hole, you are about to burn money — redesign the shot so the object is already in place and Kling animates something else.

---

*Saved 2026-04-29 by Opus 4.7 after Block 10 S3 and S4 overproduction failures. Addendum added the same day after S4 looked absurd. This file is permanent. It does not get archived. Future Claude reads this before writing the next Kling prompt.*
