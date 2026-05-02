# Closing Shot Plan — Blocks 11, 12, 13 (Aftermath + Closing Equations + End Card)

**Drafted:** 2026-04-19
**Narration blocks:** Block 11 (aftermath), Block 12 (closing equations), Block 13 (silent end card) — see `HOLY_TEXT.md`.
**Audio files:**
- `audio/E01-block11-aftermath.mp3` — NOT YET RECORDED (ElevenLabs Frank voice, very short, ~4-5s + room for a grave pause after)
- `audio/E01-block12-closing-equations.mp3` — NOT YET RECORDED (ElevenLabs Frank voice, ~10-15s)
- Block 13 is SILENT — no audio file needed, final music-note sting only if you decide to add one (currently out-of-budget per the audio rule)

**Visual style:** THIS SEGMENT DEVIATES from the Mechanism-X-through-W Kurzgesagt palette and returns to photoreal + text-on-black for the closing. Three different looks across three blocks:
- **Block 11 (Aftermath)** — photoreal to match the HUD kill section (S07-S15). Hitchcock implication only. No blood, no bodies, no gore. Empty corridors in silence.
- **Block 12 (Closing equations)** — big cream text on a near-black background. Spoken AND displayed simultaneously. This text-display IS the design (meme-language / protest-sign language, each fragment itself forwardable) and is NOT the narrator-echo text reveal that is banned for the Mechanism segments. The display IS the point of the shot.
- **Block 13 (End card)** — static text display, silent. Factual contact info only (YouTube + GitHub handle).

---

## Quick-glance summary (1 line per shot)

| Shot | One-line summary |
|---|---|
| **S75** | Unpause from S15 freeze-frame; the drone fires; off-screen kill (no body shown); visible bunker corridor briefly lit by the muzzle flash |
| **S76** | Empty bunker corridor in silence, dim emergency lighting, drifting dust, no humans visible — held for the grave pause after the narrator's line |
| **S77** | Cream text on near-black background: *"AMERICA'S FATE EQUALS YOUR CALL."* held centered, then cross-fades to *"DO NOTHING — CHINA WINS. FORWARD THIS — AMERICA LIVES."* |
| **S78** | Silent end card: cream `YouTube: Nir Strulovitz` + cream `github.com/strulovitz` on near-black background. Final music-note if budget allows, otherwise silence. Cut to black. |

---

## Shot table

| Shot | Duration | Framing | Micro-beat (start → happen → land) |
|---|---|---|---|
| **S75** | ~3s | Photoreal, matches the HUD kill section — medium shot over the drone's shoulder toward the general's room | The freeze-frame from S15 (thermal HUD on Drone #2 with crosshair locked on the general's thermal body) unpauses; the white pause-bars slide off-screen; the drone fires once (a brief muzzle-flash illuminates the corridor behind it); the general's thermal signature goes still on the HUD; no body visible in frame, only the HUD and the corridor beyond; camera holds steady. |
| **S76** | ~3-4s + grave pause | Photoreal, wide view of an empty bunker corridor | The camera pulls back out of the HUD and we see the bunker corridor in dim red emergency lighting; drifting dust motes; no people, no bodies, no blood, no gore (Hitchcock implication only); the corridor is silent except for distant ventilation hum that was already present; on the land-beat, a grave pause of dead silence holds the frame before the next block begins; camera slowly dollies backward deeper into the corridor darkness. |
| **S77** | ~12s | Centered text-display on a near-black burgundy-tinged background | Frame is near-black with a very subtle dark-burgundy wash; on the start-beat, huge cream Helvetica-weight text snaps into the center of the frame: **AMERICA'S FATE EQUALS YOUR CALL.** — narrator speaks the line in sync; the text holds for ~1 beat; on the happen-beat the first line cross-fades out and two new huge cream lines snap in stacked vertically: **DO NOTHING — CHINA WINS.** (upper half) and **FORWARD THIS — AMERICA LIVES.** (lower half) — narrator speaks these in sync; on the land-beat, the word **FORWARD** briefly pulses coral-orange (tiny accent) to cash the physical-forward-button metaphor from the war brief; camera holds steady with an almost-imperceptible slow push-in. |
| **S78** | ~5s | Centered static end card on near-black background | The text from S77 fades out; frame goes pure near-black; on the happen-beat, cream text snaps into the center stacked vertically: **YouTube: Nir Strulovitz** (upper line) and **github.com/strulovitz** (lower line); the text holds in complete silence for ~5s; camera holds steady; on the final beat, cut to pure black. No narration over this block. |

---

## How this maps to the HOLY_TEXT narration

| Narration / segment | Shots |
|---|---|
| *"Everyone inside was gone within four minutes."* (Block 11) + grave pause | S75 + S76 |
| *"America's fate equals your call. Do nothing — China wins. Forward this — America lives."* (Block 12) | S77 |
| (Block 13 — no narration, visual only) | S78 |

---

## Important design notes — why the text-display in S77 is NOT the banned narration-echo text reveal

The Mechanism shot plans (X / Y / Z / W) forbid a shot whose content is literally the words the narrator is saying at the same moment — because those would be filler that duplicates the audio track. S77 is different on two grounds and is explicitly part of Nir's locked design from `HOLY_TEXT.md` Block 12 (*"Visual: text big on black (or very dark) background. Spoken AND displayed. ~10-15s."*):

1. **The display IS the point of the shot.** The closing equations are written in meme-language / protest-sign language, each fragment designed to be itself forwardable as a screenshot. The viewer is expected to pause, read, and share. The text is the artifact, not a decoration over the audio.
2. **Per the war brief, the word "FORWARD" must appear literally** because the physical action being asked of the viewer is pressing a forward/share button. The visual-verbal redundancy is the point, not an accident.

S75 / S76 are photoreal cinema. S77 is a protest-sign text-card. S78 is a factual credit display. Each is the correct treatment for its moment — and each is distinct from the narration-echo filler that is banned in the teaching-section Mechanism clips.

---

## Production order (do not skip, do not batch)

**Blocks 11 and 12 audio first:**
1. Record Block 11 (*"Everyone inside was gone within four minutes."*) in **ElevenLabs Frank voice**, measure exact seconds, leave room for the grave pause after
2. Record Block 12 (*"America's fate equals your call. Do nothing — China wins. Forward this — America lives."*) in **ElevenLabs Frank voice**, measure exact seconds

**S75 + S76 (photoreal, continuation of HUD kill style):**
3. Reference images in **ChatGPT Image 1.5** (1:1 1024×1024 for each, 2 variants) — muzzle-flash in the dark corridor; empty corridor with dim red emergency lighting and drifting dust
4. Save to `elements/E01S75-*.png`, `elements/E01S76-*.png`
5. Kling prompts: photoreal match to HUD kill section, explicit camera motion (pulls back / dollies backward), no text, no gore — Hitchcock implication only
6. Generate in **Kling 3.0 Omni** (720p, 16:9, ~3-4s, reference image mode, Native Audio OFF)

**S77 (text-on-black closing equations):**
7. This shot can be produced in Premiere itself as a title-card animation (cream text on near-black, simple cross-fade between the two screens, coral pulse on FORWARD). No Kling call needed if Premiere can handle the animation — saves credits.
8. If Kling is preferred: reference image in ChatGPT Image 1.5 showing the final state, then Kling prompt uses start-frame → end-frame mode with the first screen as start and the second screen as end. Keep the text static (baked into the image) — do NOT ask Kling to animate the text appearing (per Lesson 21, Kling writes gibberish when animating text).

**S78 (silent end card):**
9. Produce as a static image in Premiere — cream text on near-black, held for 5s, cut to black. No Kling call needed. Saves credits.

---

## Budget note

Of these four shots, only S75 and S76 genuinely need Kling generation (photoreal corridor motion). S77 and S78 can both be produced as Premiere title-card animations from static reference images, saving ~2500 credits (approximately 10 seconds × 25 credits × 2 shots at Kling rates, plus their reference image costs). If the Premiere route is chosen for S77 and S78, only one ChatGPT Image 1.5 reference is needed per shot as a visual spec for the typographer (or as the static frame Premiere holds).

---

## What comes BEFORE this (S74) and AFTER (nothing)

- Before S75: the last clip of Mechanism W (currently planned as **S74** — the closing network-view of "IN THE DIFFERENCES").
- After S78: the video ends. Cut to pure black. Upload to YouTube.
