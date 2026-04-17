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

"The basic idea is simple: an ant colony is a living computer, even though each ant is dumb. But as a colony, they combine into an intelligent super-organism. Pathfinding. The piano movers problem. All of it with no leader. No General Ant. Our competitors only talk the talk as marketing hand-waving: swarm intelligence. Emergence. We are the first to walk the walk. We are the first to really do it. Remember Devastator from the Transformers? A group of separate machines that combined into one giant robot far more powerful than any of them alone. Our drones do the same thing — except they combine their minds, not their bodies. And instead of science fiction, it is real computer science."

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
6. Generate in OpenArt: ChatGPT Image 1.5, 16:9, 2 variants, pick best
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
- Aspect ratio: 16:9
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
