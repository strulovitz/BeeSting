# BeeSting Part 1 — Video Production Handoff

**Written by:** Laptop Windows Claude, 2026-04-16 evening
**For:** The next Claude Code session continuing the video production (likely Desktop Windows Claude)
**Source of truth:** `PART_1_WAR_BRIEF.md` — read this FIRST, end to end.

**Where to find the remaining scenes:** In `PART_1_WAR_BRIEF.md`, search for **"SHOT LIST"** — that section has every remaining clip planned with durations, reference image descriptions, and which narration text goes with each clip. The locked narration texts for all 4 mechanisms (X, Y, Z, W) are earlier in the same file — search for **"MECHANISM X"**, **"MECHANISM Y"**, **"MECHANISM Z"**, **"MECHANISM W"** to find each one.

**Direct link:** https://github.com/strulovitz/BeeSting/blob/master/PART_1_WAR_BRIEF.md

---

## What has been done

### All 4 mechanism narrations LOCKED
- Mechanism X (SMS ladder + divide-and-conquer) — in the war brief
- Mechanism Y (jamming / near-field physics) — in the war brief
- Mechanism Z (no head to cut off / piranhas to Great White) — in the war brief
- Mechanism W (finds the invisible / cross-referencing sensors) — in the war brief

### Book updated
- TheDistributedAIRevolution chapter_11.md — new section "But we have AI — what does the brain add to the nose?" covering decoy discrimination, points to vectors, multi-modal consensus, scaffolding+AI two-layer architecture. Libraries named: NumPy, SciPy, FilterPy.

### 6 completed shots (the entire EXTERIOR sequence)

| Shot | File prefix | Image | Audio | Video | Duration | Description |
|---|---|---|---|---|---|---|
| S00 | E01S00-emoji-equation | .png (elements/) | .mp3 (audio/) | N/A (image in Premiere) | 6 sec | Emoji equation on black: China+Israel=USA skull. 2 sec silence, 3 sec narration, 1 sec silence. |
| S01 | E01S01-missile-launch | .png (elements/) | .mp3 (audio/) | .mp4 (clips/) | 5 sec | Missile launches at night from mobile transporter. |
| S02 | E01S02-drone-swarm-descending | A1+A2 .png (elements/) | .mp3 (audio/) | .mp4 (clips/) | 9 sec | Drone swarm descends toward mountain. Start/end frame mode. |
| S03 | E01S03-bunker-exterior | A3 .png (elements/) | .mp3 (audio/) | .mp4 (clips/) | 8 sec | Bunker exterior, imposing blast doors. Reference image mode. |
| S04a | E01S04a-drone-sacrifice | .png (elements/) | (shares S04 audio) | .mp4 (clips/) | 3 sec | One drone explodes on the vent grate to breach it. |
| S04b | E01S04b-drones-through-blown-grate | .png (elements/) | .mp3 (audio/) | .mp4 (clips/) | 5 sec | Drones stream through the destroyed grate into the tunnel. |

Audio for S04: narration "No radio reaches in or out. And yet — they came in through the air vents." plays across both S04a and S04b.

Total exterior sequence: ~36 seconds.

### Narration text per shot

| Shot | Narration text | Audio duration |
|---|---|---|
| S00 | "Israeli invention exists. Chinese production starting." | 3 sec |
| S01 | "This ballistic missile is not carrying a bomb. It is carrying something much worse." | 4 sec |
| S02 | "Inside it — a swarm of small cheap drones. Military-hardened. Disposable. Nothing exotic. Anyone can build them." | 7 sec |
| S03 | "They flew into one of our most secure military bunkers — buried deep under a mountain, walls lined with metal." | 6 sec |
| S04 | "No radio reaches in or out. And yet — they came in through the air vents." | 4 sec |

---

## What needs to be done next

### Shot #5 onward — INSIDE the bunker

The next shots go inside the bunker corridors. This is the ATTACK section from the war brief structure table (lines 248-249). The narration is:

"The basic idea is simple: an ant colony is a living computer, even though each ant is dumb. But as a colony, they combine into an intelligent super-organism. Pathfinding. The piano movers problem. All of it with no leader. No General Ant. Our competitors only talk the talk as marketing hand-waving: swarm intelligence. Emergence. We are the first to walk the walk. We are the first to really build it. Remember Devastator from the Transformers? A group of separate machines that combined into one giant robot far more powerful than any of them alone. Our drones do the same thing — except they combine their minds, not their bodies. And instead of science fiction, it is real computer science."

Then the corridor sequence transitions to night-vision green HUD POV with white text overlays: TARGET ACQUIRED, GENERAL X CONFIRMED, MISSION OBJECTIVE: TERMINATE.

Then THE PAUSE (frozen frame with white pause rectangles).

Then the feature tease (5 observations).

Then Mechanisms X, Y, Z, W (all narration texts locked in the war brief).

Then unpause, kill, aftermath, closing equations, end card.

See the full shot list in PART_1_WAR_BRIEF.md for every clip planned with durations.

---

## Production workflow (follow this for EVERY shot)

1. Write narration text in Downloads/narration_text.txt
2. Generate in ElevenLabs with "Frank - Wise, Deep and Motivational" voice
3. Download, note the duration in seconds
4. Apply breathing room rule: +25% of narration duration, minimum +1 sec, maximum +3 sec = video clip duration
5. Write OpenArt reference image prompt in Downloads/openart_prompt.txt
6. Generate in ChatGPT Image 1.5, 1:1 1024×1024, 2 variants, pick best
7. Download, rename to E01S##-description.png, save to elements/ in repo
8. Write Kling prompt in Downloads/kling_prompt.txt
9. Generate in Kling 3.0 Omni: 720p, NO audio, reference image mode (or start/end frame for chains)
10. Download, rename to E01S##-description.mp4, save to clips/ in repo
11. Also copy renamed .mp3 to audio/ in repo
12. Import video + audio into Premiere, place after previous shot
13. Audio starts 1-2 seconds into the clip (breathing room)
14. Commit and push everything to GitHub

---

## 🚫 Audio rule — CRITICAL (do not violate)

The final BeeSting video has **ONLY ElevenLabs narration in the Frank voice**. No music. No ambient sound. No sound effects. No Kling native audio.

This is a **money constraint**, not a creative choice. Kling's Native Audio feature and licensed music are both out of budget. Any silence in a shot is REAL silence in the final cut — no music covers gaps.

**Implications:**
- Plan shot durations so narration covers the visual OR the silence is a deliberate dramatic beat (Hitchcock pause, aftermath, end-card hold). Avoid long silent shots that exist only because the narration ran out before the video did. Err SHORTER when unsure.
- Kling prompts describe VISUALS ONLY — never sound, never music, never ambient. Native Audio toggle stays OFF every time.
- Do NOT say "we'll add music later to cover the silence." There is no music pass. What the viewer hears in the rough cut is what the viewer hears in the final cut.

## Kling settings (NEVER change these without checking with Nir)

- Model: Kling 3.0 Omni
- Resolution: 720p
- Native Audio: **OFF** (always — see Audio rule above)
- Duration: 3-15 seconds (any integer), matched to narration + breathing room
- Two modes: reference image (standalone clips) or start/end frame (chains)
- Cost: 25 credits per second of video

## ElevenLabs settings

- Voice: "Frank - Wise, Deep and Motivational"
- Subscription: $6/month, ~30K credits available (~30 min speech)
- Just paste text, generate, download

## OpenArt reference image settings

- Model: ChatGPT Image 1.5
- Aspect ratio: 1:1 1024×1024
- Variants: 2 (pick best)
- Cost: 50 credits per image (2 variants)

---

## Budget status as of end of session

| Resource | Used | Remaining |
|---|---|---|
| OpenArt credits | ~1,200 (6 images x 50 + 6 clips ~900) | ~18,100 |
| ElevenLabs credits | ~550 | ~30,900 |

Plenty of both for the remaining ~44 clips.

---

## Naming scheme

All files follow: E01S##-description.ext
- .png = reference image (in elements/)
- .mp3 = narration audio (in audio/)
- .mp4 = video clip (in clips/)
- Same name for corresponding audio/video/image — only suffix differs

Chain transition images add a suffix: E01S02-A1-drones-high.png, E01S02-A2-drones-at-vent.png

---

## Breathing room rule

Add 25% to the narration duration. Minimum +1 second. Maximum +3 seconds. The breathing room sits at the BEGINNING of each clip — 1-2 seconds of pure visual before the narrator speaks.

---

## Lessons learned today (DO NOT repeat these mistakes)

1. **Kling cannot do complex physics.** Do not ask Kling to show drones exiting a missile nose cone, or camera pulling back to reveal a wide shot from a close-up. Keep prompts SIMPLE — one action, one camera angle.

2. **Split long narrations into shorter clips.** If narration is 12+ seconds, split into two ElevenLabs recordings and two video clips. Kling is more reliable on shorter clips.

3. **Reference image mode is more reliable than start/end frame mode** for most shots. Use start/end frame only when you genuinely need a continuous seamless shot (corridor sequences, underwater sequences).

4. **The sacrifice drone was Nir's idea and it was brilliant.** Drones are NOT insect-sized. They cannot slip through a ventilation grate. One drone must breach it with an explosive first. This kind of tactical realism matters — do not skip it.

5. **Keep Kling prompts short and simple.** 2-3 sentences max. Describe what happens, not how it should feel. Kling does not understand mood words well — it understands action words.

6. **Voice first, then video.** Always generate the ElevenLabs narration FIRST, measure its exact duration, THEN calculate the video clip duration. Never guess.

7. **Save to Downloads with the E01S## naming scheme immediately.** Nir uses the Downloads folder for Premiere. The renamed files in Downloads are his working copies.

8. **Night-vision HUD is phosphor GREEN (like real NVGs), not red (Terminator).** White text overlays. Not "military green" (that sounds like uniform color to Kling).

9. **No Premiere effects needed.** Nir is a beginner. Just stitch clips + lay audio + trim. No transitions, no effects, no audio mixing.

10. **ALWAYS look at the reference PNG before writing the Kling prompt.** Use the Read tool on the actual `elements/E01S##-*.png` file before drafting or editing `Downloads/kling_prompt.txt`. Describe what is literally in the image (positions, colors, lighting, specific doorways, characters) and write the motion prompt relative to those concrete elements ("drones bank right through the red-lit doorway on the right side of the room" — not vague "continues deeper"). Kling 3.0 Omni costs 25 credits per second — a 5-second clip is 125 credits. On 2026-04-18 the S06 prompt was written without viewing the PNG, Kling left the drones static and flew the camera alone, and we burned a full regen to fix it. One Read call saves 125+ credits. Never write a Kling prompt from imagination when the reference image is on disk.

11. **ALWAYS remind Nir to import the new clip to Premiere after every clip lands.** Every time a clip is renamed and committed to `clips/`, end the response with a one-line Premiere import reminder ("👉 Now drag `E01S##-*.mp4` into Premiere on the video track after the previous clip 🎞️"). Nir works on many clips in parallel with other tasks and it is easy to forget the Premiere step between OpenArt download and the next shot. The reminder is not optional — do it every single time, not "the first time each session."

12. **NEVER MOVE audio/clip/image files out of Downloads — COPY them, never move.** Nir's Premiere workflow drags files directly from the Downloads folder. If Claude moves a file from Downloads into `clips/` (or `audio/`, `elements/`), Nir cannot find it to drag into Premiere and has to hunt through the repo folders. Instead: `cp` the file to the repo with the clean `E01S##-description.ext` name for the git commit, AND keep/rename a copy in Downloads with the same clean name. Downloads is Nir's active working folder; the repo is the permanent archive. Both must have the file. Rule: **rename in place in Downloads first, then `cp` into the repo**, never `mv`.

14. **NEVER SAY "OPENART" — always name the specific engine.** "OpenArt" is the hosting site, not a model. Saying "generate in OpenArt" is ambiguous — Nir cannot tell if Claude means **ChatGPT Image 1.5** (image, cheap) or **Kling 3.0 Omni** (video, burns 25 credits/second). When the wrong engine is used it wastes real money. **Always write the specific engine name in every announcement, prompt file, and instruction:**
    - Images: **ChatGPT Image 1.5** (the only image model we use)
    - Videos: **Kling 3.0 Omni** (the default video model) or **Kling Avatar** (only for lip-sync) or **Veo 3.1** (backup cinematic, 4/6/8s only)
    - Audio: **ElevenLabs Frank voice**
    Also ban the bare word "OpenArt" in Lesson 13 announcement templates — the template is `**S## — 2-3 word description — ChatGPT Image 1.5**` or `**S## — 2-3 word description — Ns — Kling 3.0 Omni — ref: file.png**`. Never `**S## — 2-3 words — OpenArt**`. Same rule in all prompt filenames, comments, docs, and git commit messages going forward. Rewriting "OpenArt" as the engine name in older docs is fine but not urgent — what matters is every NEW line says the engine, not the host. Rule set 2026-04-17 by Nir during video-production work, re-locked 2026-04-18 after a relapse.

15. **ASPECT RATIO IS SET IN THE GUI, NEVER IN THE PROMPT TEXT.** Both ChatGPT Image 1.5 and Kling 3.0 Omni have explicit aspect-ratio dropdowns in the OpenArt GUI. Writing "16:9 aspect ratio" or "1:1 framing" or "cinematic widescreen" inside the prompt text competes with the GUI setting and sometimes produces wrong results. The prompt describes the scene; the GUI sets the canvas. Do not mix them.

16. **Reference images are 1:1 1024×1024, not 16:9.** Verified 2026-04-18: all 8 existing S01-S06 reference images in `elements/` are 1024×1024 square. Only the text-heavy S00 emoji equation card was 1280×720. The docs in `PART_1_WAR_BRIEF.md`, `HANDOFF_VIDEO_PRODUCTION.md`, and `PART_1_SHOT_LIST.md` said 16:9 — they were WRONG and are being corrected. `PART_1_ELEMENTS.md` had it right from the start (1:1 1024×1024). **The canonical ChatGPT Image 1.5 setting for BeeSting references is 1:1 1024×1024, Medium or Pro quality, 2 variants.** Kling 3.0 Omni video clips stay at 16:9 (that is a separate setting).

17. **NEVER describe subjects "getting larger / closer / clearer" in a Kling prompt — Kling inflates them literally.** On 2026-04-18 the S12 prompt said the two human thermal signatures in the far corridor should "get slightly larger and clearer as the drone closes the distance". Kling took it literally — the humans floated toward the camera and inflated like balloons instead of the drone's camera moving forward. **Rule:** describe ONLY what the CAMERA does (forward creep, slight pan, static hold) and what background / atmosphere / HUD elements do (boot-up lines, scan lines, sparks, smoke drift). **Do NOT describe foreground subjects (people, drones-in-frame, props) as growing, shrinking, approaching, or receding** — Kling will animate the subject itself rather than the camera. If a subject must appear to move closer, either say "camera moves toward them" (not "they grow") or simply omit any motion cue about them and let them stay in place. When in doubt, tell Kling LESS about subjects — a static subject is a correct subject; a described-moving subject is a lottery ticket.

18. **Kling does NOT infer ANY scene element from the reference image — re-describe every persistent element (HUD, background, props, characters, environments) in the Kling prompt itself.** On 2026-04-18 the S13 Kling prompt dropped the HUD crosshair because it was not named; on 2026-04-18 the S27 Kling prompt dropped the cream doorway and the map panel for the same reason. **Rule:** whichever elements must appear in the generated clip — crosshairs, compass bars, corner readouts, banners, background doorways, side props, secondary characters, map overlays, frame borders, scan cones, color scales — must be NAMED in the Kling prompt, every time, even if they are obviously in the reference image. Kling treats the reference image as a style/composition hint, not as a frame-one commitment. If the element is not in the prompt, Kling may drop it, relocate it, or animate it weirdly. The rule is "name every important element in every Kling prompt, every time, regardless of how obvious it seems from the ref."

19. **"Tick" is a vague word — Kling interprets it as flashing / blinking.** On 2026-04-18 "readouts tick slightly" in the S13 Kling prompt produced elements that almost blinked on/off instead of a steady digital counter. **Rule:** avoid vague motion words. Be concrete about HUD element motion: "the REC timer counts up one second at a time", "the compass bar shifts slowly by one degree", "the altitude number changes by small integer steps (3.2, 3.1, 3.0)". Use numbers and units, not abstract verbs. Same rule for "flicker", "shimmer", "pulse" — all produce unpredictable blinking. Better: "remains steady" or "changes smoothly by a small amount".

20. **EVERY Kling prompt MUST include an explicit camera motion. "Hovers", "holds", "static", "hovers still" = wasted credits.** On 2026-04-18 multiple Kling prompts used camera verbs like "hovers" and "holds position" — Kling produced effectively frozen frames with only HUD elements animating, which looks like a still image with blinking overlays and burns the full 125-credit clip cost for no real motion. **Rule:** every Kling prompt must give the drone / camera a concrete movement verb: "drifts smoothly forward", "slowly descends", "slowly pushes in", "dollies forward by about half a meter", "glides to the right by a short distance", "gently banks down". Even a subtle one-meter creep is enough to feel alive. NEVER "hovers" or "holds". The viewer's eye needs the frame to be breathing; a frozen frame reads as a crashed video. Apply Lesson 17 alongside this one: the CAMERA moves, the SUBJECTS (people, props) stay in their positions. Camera motion + subject stillness = correct Kling clip. Camera stillness = wasted credits.

21. **Do NOT ask Kling to animate TEXT appearing or changing on a screen — Kling writes gibberish.** On 2026-04-18 the S18 Kling prompt said "the phone screen then wipes to a clean cream voice-call indicator" and Kling interpreted the wipe as writing new text on the screen — which came out as unreadable gibberish that Nir described as "looks more like video than voice." Kling 3.0 Omni is a video model, not a typography model — any on-screen text it synthesizes at animation time comes out wrong. **Rule:** never describe text appearing, changing, scrolling, or being typed during a Kling clip. If text must change, bake the change into TWO separate reference images (before / after) and use start-frame / end-frame mode — or simply hold whatever text was already rendered by ChatGPT Image 1.5 in the reference image and let Kling preserve it unchanged. Safer still: describe the screen change as an ICON ENLARGING or a COLOR HIGHLIGHT, never as new text appearing. Example: instead of "the screen writes 'CONNECTED'", say "a large cream headphone icon fills the screen."

22. **Do NOT call drones "queen" / "worker" + amber + crown WITHOUT explicitly banning bees — ChatGPT Image 1.5 draws a literal bee.** On 2026-04-18 the S25 image prompt described "the amber queen drone with her amber crown icon floating above her antenna, four cream propellers" and ChatGPT Image 1.5 rendered an actual insect bee instead of a quadcopter drone. The combination of *queen + worker + amber body + crown* is so strongly associated with bees in training data that even explicit drone / antenna / propeller language can be overridden. **Rule:** every BeeSting Mechanism prompt that involves queen/worker drones MUST include an explicit negative clause banning insect / bee / wings / stinger / antennae-of-insect imagery, AND affirmatively describe the shape in mechanical terms. Example good wording: *"quadcopter drone — a simple square mechanical body with four circular propellers at the corners, a single thin straight antenna line on top (NOT antennae of an insect). NOT A BEE, NOT AN INSECT, NOT A WASP — this is a flying machine. The 'crown' marking the queen is a small stylized crown icon floating as a symbolic tag above the drone's body, not part of its anatomy."* Apply this to S24, S25, S26, S27, S28, S29 and any future queen/worker shots in any Mechanism section.

13. **MINIMAL ANNOUNCEMENTS — Nir knows the tools, do not wall-of-text him.** Nir has used ChatGPT Image 1.5, Kling 3.0 Omni, ElevenLabs, and Premiere every day for months. He does NOT need numbered step-by-step instructions, settings lists, or encouragement. When a prompt is saved to Downloads, announce it in ONE line with only the must-know items. Templates:
    - **Image prompt:** `**S## — 2-3 word description — ChatGPT Image 1.5**` (the model name is required every time so Nir does not accidentally generate a video and burn credits)
    - **Video prompt:** `**S## — 2-3 word description — Ns — ref: E01S##-*.png**` (scene number, tiny description, duration in seconds, reference image filename; for start/end frame chains, name both frames)
    - **Audio (ElevenLabs):** `**Block ## — 2-3 word description — Frank voice**`
    No numbered lists. No settings blocks. No "fingers crossed" flavor text. No enumerated instructions. Just the scene, the description, and the critical parameter. If Nir wants more detail he will ask. The LESS Claude writes, the MORE likely Nir notices the one important detail. Walls of text bury the signal.

23. **No title cards that echo the narration. No giant text-reveal endings.** A shot whose content is literally the words the narrator is saying at the same moment is filler. Examples to avoid: opening a mechanism segment with an "Observation 3" text card while the narrator says *"Observation three said..."*; closing with a huge "THAT IS MAGIC" text slide while the narrator says *"That is magic."* The viewer already HEARS the narration — the visual's job is to COMPLEMENT the audio, not transcribe it. Parallel tracks multiply each other; redundant tracks cancel out. Inline diagram annotations (a "2 m" label on a measure line, a "JAMMING" concept-identifier on a character with hands over ears) are fine — those are diagram UI, not narration echo. Giant text slides that ARE the narration are not fine. Rule locked 2026-04-19 after Mechanism Y's first draft opened with an "Observation 3" title card and closed with a "THAT IS MAGIC" text reveal; both were rejected.

24. **Kling cannot preserve character identity across independent clips — no recurring characters, no story arcs across clips.** Each Kling 3.0 Omni clip is generated from its own fresh reference image; the "same character" described in the prompt for clip A will look visually different in clip B because the reference images were generated independently. A shot plan that depends on a villain or hero repeating across multiple clips is a broken premise on current video-model technology. Build each clip as an independent scene with generic geometric characters representing the abstract concept, not specific recurring cast. This matches how Mechanism X worked — S16-S21 had a character holding a phone, but no assumption was made that S16's character is visually the same person as S18's character; each was a fresh generic geometric person illustrating that clip's concept. Rule locked 2026-04-19 after a Mechanism Y draft proposed a recurring "Jammer villain" character across 9 shots; that draft was rejected because Kling cannot deliver identity continuity on the reference-image pipeline.

25. **"Cool" means clear-and-engaging, not funny-cartoonish.** When the brief calls for visuals to be "cool," that means maximum clarity per clip, abstract concepts illustrated with Kurzgesagt-explainer polish, confident flat-vector motion graphics. It does NOT mean slapstick villain, recurring jokes, cartoon personalities with story arcs, or comedy. BeeSting is a serious explainer that happens to use flat 2D motion graphics as its visual language — it is not a cartoon. Strip all character biographies, story arcs, villain personalities, running jokes, and recurring-character descriptions out of any shot plan. Kling is a limited model; the little it can carry must carry the information in the clearest, most engaging form possible — that clarity is the "cool" the brief is asking for, not cartoon humor.

26. **Match the Mechanism X shot plan template exactly for subsequent mechanisms (Y, Z, W).** `MECHANISM_X_SHOT_PLAN.md` is the canonical shot-plan format. When planning Y / Z / W: copy its structure and tone exactly — simple shot table (columns: Shot, Duration, Framing, Micro-beat), narration-to-shot mapping table, production-order block, Kurzgesagt palette intro, anti-bee clause. Do NOT add new structural sections like "Story arc," "Character cast," or "Recurring-villain description block." Do NOT invent a new cinematic approach. Strip the plan down to what X has. If a future mechanism's plan has grown beyond X's structure, that growth is probably bad and should be deleted back down.

27. **`mv` not `cp` when renaming a file; `cp` when moving from Downloads into the repo.** Renaming a file within Downloads (e.g. from ElevenLabs's auto-generated `ElevenLabs_2026-04-19T09_28_50_Frank - Wise...mp3` to the clean `E01-block08-mechanism-y.mp3`) uses `mv` — one canonical name, no original left behind. Copying the cleanly-renamed file from Downloads INTO the repo (`audio/`, `clips/`, `elements/`) uses `cp` — Downloads keeps its working copy with the clean name for the Premiere drag-in workflow per Lesson 12. End state: exactly one canonical name in Downloads, exactly one copy in the repo, zero originals-with-long-auto-generated-names lying around. Rule locked 2026-04-19 after a mid-session rename used `cp` and left a long-named original in Downloads next to the clean-named duplicate.

28. **Every clip is independent — alternating framings across consecutive clips + micro-beat (start → happen → land) in every clip.** Restating the three engagement tricks from `MECHANISM_SECTION_VISUAL_STYLE.md` because it is easy to drift off them while proposing things like a recurring-villain story arc. (a) Each clip stands alone — no dependency on what came before. (b) Consecutive clips must NOT share composition — wide → close → side → POV → top-down → isometric, alternate deliberately. (c) Every clip has a three-step micro-story inside its 6 seconds — something enters the frame, something changes or moves, something clicks into its final landing position. Even if the scene subject stays constant across the micro-beat, the motion arc is what keeps the eye alive — a static pose for 6 seconds is wasted credits.

29. **Include a one-line-per-shot summary table at the top of every mechanism shot plan.** The detailed shot-by-shot table with full micro-beat descriptions is necessary for generating the prompts, but it is hard to eyeball the whole mechanism at once. A compact 1-line-per-shot summary block at the top of the shot plan (columns: Shot, One-line summary) lets the whole flow be verified in under a minute before any credits are spent. Rule locked 2026-04-19; Mechanism Y now has this block, and Mechanisms Z and W should also have it when their plans are written.

---

## Files in the repo

```
BeeSting/
  PART_1_WAR_BRIEF.md          -- THE source of truth (narration, structure, shot list, everything)
  HANDOFF_VIDEO_PRODUCTION.md  -- this file
  elements/
    E01S00-emoji-equation.png
    E01S01-missile-launch.png
    E01S02-A1-drones-high.png
    E01S02-A2-drones-at-vent.png
    E01S03-A3-bunker-exterior.png
    E01S04a-drone-sacrifice.png
    E01S04b-drones-through-blown-grate.png
  audio/
    E01S00-emoji-equation.mp3
    E01S01-missile-launch.mp3
    E01S02-drone-swarm-descending.mp3
    E01S03-bunker-exterior.mp3
    E01S04-drones-enter-vent.mp3
  clips/
    E01S01-missile-launch.mp4
    E01S02-drone-swarm-descending.mp4
    E01S03-bunker-exterior.mp4
    E01S04a-drone-sacrifice.mp4
    E01S04b-drones-through-blown-grate.mp4
  voice/
    narrator_frank_reference.mp3  -- ElevenLabs "Frank" voice sample (backup reference)
```

---

## Critical rules (from PART_1_WAR_BRIEF.md, memorize these)

- Narrator is OFF-SCREEN. No face, no lips, no character. Just voice over visuals.
- No "our system" / "our invention" / "our topology" in narration
- No dollar figures
- No mention of Nir, Israel, Elbit, Rafael in the narration body
- Credibility is in the end card only: "YouTube: Nir Strulovitz" + "github.com/strulovitz"
- Night-vision HUD: phosphor green tint, white text overlays
- No gore, no blood, no body shown — Hitchcock implication only
- "Forward this = America lives" is the closing line
- Every word spoken is literal truth; every image is clearly illustrative

---

*Read PART_1_WAR_BRIEF.md first. This handoff tells you what was done and how. The war brief tells you what to do and why.*
