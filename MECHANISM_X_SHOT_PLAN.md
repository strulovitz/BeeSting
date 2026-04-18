# Mechanism X — Shot Plan (16 clips, ~6 seconds each)

**Locked:** 2026-04-18
**Narration block:** Block 7 (SMS ladder + divide-and-conquer, ~95 seconds, see `HOLY_TEXT.md`)
**Visual style:** Kurzgesagt-style flat 2D motion graphics, duotone palette (deep navy background + warm amber highlight + cream accents), per `MECHANISM_SECTION_VISUAL_STYLE.md`.
**Engagement tricks applied:** 2× ~6s splits instead of 8× ~12s, micro-beat per clip (start → happen → land), alternating camera framings across consecutive clips.

Total runtime: 16 × 6s = 96s. Matches Block 7 narration (95s) with ~1s slack.

---

## Shot table

| Shot | Duration | Framing | Micro-beat (start → happen → land) |
|---|---|---|---|
| **S16** | 6s | Wide, character centered | Character holding phone flat; video call on screen pixelates and freezes into colored blocks; character's eyebrows drop in frustration. |
| **S17** | 6s | Tight close-up on phone screen | Frozen video distorts further; cream "RECONNECTING..." label slides in at top; the image collapses into static blocks. |
| **S18** | 6s | Side profile of character | Character lowers phone from face; taps a "switch to voice" button; shoulders drop, small relieved smile lands. |
| **S19** | 6s | Over-the-shoulder POV | Phone now shows clean voice-call UI; a glowing amber "Voice" icon pulses once; character's posture stays relaxed. |
| **S20** | 6s | Top-down flat on phone | Signal bars drop lower; voice UI collapses to SMS messaging view; the first short text bubble pops in. |
| **S21** | 6s | Close-up on the text bubbles | Three short text bubbles pop in one after another, each a bright amber rectangle landing crisply against navy. |
| **S22** | 6s | Isometric view, one small drone | Small flat-vector drone hovers; a tiny amber text bubble emerges from its antenna; another drone across the frame answers with an inbound bubble. |
| **S23** | 6s | POV tracking alongside the drone | Drone flies forward; text bubble trails a short distance and lands in the receiving drone ahead; a small "sent" check-mark icon lands. |
| **S24** | 6s | Wide hexagonal formation | Queen drone pops in at the center of the frame; five worker drones pop in one at a time around her in a circle. |
| **S25** | 6s | Close-up on the queen | Queen emits outgoing amber text bubbles toward the workers; a beat later, smaller inbound bubbles return to her from the workers. |
| **S26** | 6s | Wide split-screen (2–4 small panels) | Each panel shows one worker in a separate bunker corridor doing her own scan; the panels light up one at a time as workers activate. |
| **S27** | 6s | Close-up on a single worker | Worker scans a doorway; a small map fragment snaps into her panel; an amber result bubble floats outward on the final beat. |
| **S28** | 6s | Wide, back on the queen at center | Result bubbles from all workers fly back toward the queen; her center starts to glow as each bubble arrives. |
| **S29** | 6s | Close-up on the queen | Inside her amber glow, the combined bunker map assembles piece by piece; the final map snaps into place in one beat. |
| **S30** | 6s | Wide, outside view of a sealed metal room | External "Cloud" icon drops toward the sealed room; a red X rejects it; inside the room, the drones continue texting unaffected. |
| **S31** | 6s | POV tracking the drones through three environments | Three quick micro-vignettes stitched: bunker corridor → underwater → Faraday cage; the drones carry their amber-glow hive-mind with them across all three. |

---

## How this maps to the Block 7 narration (see `HOLY_TEXT.md`)

| Narration segment | Shots |
|---|---|
| *"You know how when you are on a video call...reception gets bad..."* | S16, S17 |
| *"...turn off the video and switch to voice only — and suddenly you can hear each other again..."* | S18, S19 |
| *"...drop to text messages. SMS. Almost no information..."* | S20, S21 |
| *"The drones in the swarm are always at SMS level. By choice..."* | S22, S23 |
| *"The queen gets a task. She splits it into smaller pieces. She sends each piece to one worker drone as a short text..."* | S24, S25 |
| *"Each worker thinks about her own piece..."* | S26, S27 |
| *"...sends back a short answer. The queen collects all the short answers and combines them into one final answer."* | S28, S29 |
| *"...they can do this anywhere text messages can travel...Underwater...metal bunker...Faraday cage..."* | S30, S31 |

---

## Production order (do not skip, do not batch)

Generate shots one at a time per `HANDOFF_VIDEO_PRODUCTION.md` workflow:

1. Reference image in ChatGPT Image 1.5 (1:1 1024×1024, 2 variants)
2. Save to `elements/E01S##-description.png`
3. Kling prompt describes Kurzgesagt style + THIS CLIP's framing + THIS CLIP's micro-beat (start → happen → land) + THIS CLIP's 6-second duration
4. Generate clip in Kling 3.0 Omni (720p, 16:9, 6s, reference image mode, Native Audio OFF)
5. Save to `clips/E01S##-description.mp4`, keep copy in `Downloads/` for Premiere (per Lesson 12)
6. Remind Nir to drag into Premiere (per Lesson 11)

Iterate shot-by-shot. No batching 16 prompts at once.
