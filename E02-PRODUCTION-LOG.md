# BeeSting Ep2 — Production Log

Tracks every generated file, its duration, and clip math for each block.
Rule: clips × 6s must be ≥ audio duration. Audio wins if they disagree.

---

## 🚨 MANDATORY CHECKLIST — EVERY SINGLE FILE, NO EXCEPTIONS 🚨

**After Nir downloads ANY file (audio MP3, reference PNG, video MP4 — anything):**

### Step 1 — Rename in Downloads
```
mv "C:\Users\nir_s\Downloads\<ugly-auto-name>" "C:\Users\nir_s\Downloads\<proper-E02-name>"
```

### Step 2 — Copy to BeeSting repo
```
cp "C:\Users\nir_s\Downloads\<proper-E02-name>" "C:\Users\nir_s\Projects\BeeSting\<audio|elements|clips>\"
```

### Step 3 — Remind Nir to drag into Premiere
**Say explicitly: "Now drag `<filename>` into Premiere!"**
If Nir forgets this step the whole timeline breaks. Claude must say it every time without being asked.

### Step 4 — Commit and push to BeeSting repo
```
cd C:\Users\nir_s\Projects\BeeSting && git add <file> && git commit -m "<message>" && git push
```

**This checklist runs for EVERY file. No skipping. No assuming Nir will remember.**

---

---

## Block 1 — Equation hook + Golden Gate collapse

| File | Type | Duration |
|---|---|---|
| E02-block01-equation-hook.mp3 | ElevenLabs / Samantha (Madeline) | 11s |
| E02-block01-emoji-equation.png | Static frame (reused from E01S00) | ~3s in Premiere |
| E02-block01-clip-A-golden-gate-rust.mp4 | Kling 3.0 Omni | 6s |
| E02-block01-clip-B-golden-gate-collapse.mp4 | Kling 3.0 Omni | 6s |

**Premiere timeline (confirmed by Nir 2026-04-24):**
- 0:00–0:05 → equation frame (5s, static PNG) — narration plays
- 0:05–0:08 → Clip A (3s, Golden Gate rust) — narration plays
- 0:08–0:11 → Clip B (3s, Golden Gate collapse) — narration ends exactly here
**Audio:** 11s. Total visuals = 11s. Perfect match. No SFX ever.
**Kling mode:** start/end frame. Clip A: Image1→Image2. Clip B: Image2→Image3.
**Reference images:** Image1 ✅ Image2 ✅ Image3: pending.
**Status:** Block 1 COMPLETE ✅ — Nir approved.

---

## Block 2.1 — Samantha studio open

| File | Type | Duration |
|---|---|---|
| E02-block02.1-samantha-studio-open.mp3 | ElevenLabs / Samantha (Madeline) | 35s |

**Status:** Audio ✅. Visual: Samantha talking head (ChatGPT Image 1.5 ref → Kling Avatar lip-sync) — COMPLETE ✅ 35s, chyron added in Premiere.

---

## Block 2.2 — Tony field open

| File | Type | Duration |
|---|---|---|
| E02-block02.2-tony-field-open.mp3 | ElevenLabs / Tony (Joey) | 10s |

**Kling Avatar rule (updated 2026-04-25):** Kling Avatar sometimes adds ~2 bad seconds at the end — check each clip and trim only if needed. Not always necessary.

**Status:** Audio ✅ 10s. Clip ✅ trimmed to 10s in Premiere.

---

## Block 2.3 — Vox pop (10 characters)

| # | Character | File | Voice | Duration | Status |
|---|---|---|---|---|---|
| 1 | Surfer dude | E02-block02.3-vox01-surfer.mp3 | Sam - Relaxed | 5s | ✅ Clip in Premiere |
| 2 | Beach babe | E02-block02.3-vox02-beach-babe.mp3 | Gracie Valley | 4s | ✅ Clip in Premiere |
| 3 | Latino guy | E02-block02.3-vox03-latino.mp3 | Antonio - Youthful and Direct | 3s | ✅ In Premiere |
| 4 | Young Black student | E02-block02.3-vox04-black-student.mp3 | Misha - Friendly, Bold, and Engaging | 3s | ✅ In Premiere |
| 5 | Redhead cheerleader | E02-block02.3-vox05-cheerleader.mp3 | Kristen - Upbeat social media influencer | 3s | ✅ In Premiere |
| 6 | Skater dude | E02-block02.3-vox06-skater.mp3 | Brayden - Cheery, Clear and Chill | 3s | ✅ In Premiere |
| 7 | Asian bartender | E02-block02.3-vox07-bartender.mp3 | Sapphire - Sweet, Youthful, and Clear | 4s | ✅ In Premiere |
| 8 | Hippie old guy | E02-block02.3-vox08-hippie.mp3 | Dar - Southern California Male Voice | 4s | ✅ In Premiere |
| 9 | Mother with children | E02-block02.3-vox09-mom.mp3 | Amy - Upbeat and Excited | 3s | ✅ In Premiere |
| 10 | Beach babe returns | E02-block02.3-vox10-beachbabe-return.mp3 | Gracie Valley - Seductive and Sassy | 7s | ✅ In Premiere |

**Note on Vox03:** Script line changed from "The price, dude." to "The price, Ese. BIG AI is for the one percent. Not for me." — "Ese" capitalized so ElevenLabs pronounces it correctly as the Latino slang.

---

## Block 2.4 — Tony closer with DeepSeek Moment² reveal

| File | Type | Duration |
|---|---|---|
| E02-block02.4-tony-deepseek-reveal.mp3 | ElevenLabs / Tony (Joey) | 37s |

**Status:** COMPLETE ✅ — Audio 37s, Kling Avatar clip 37s, in Premiere. No overlay graphic, no chyron (dropped for simplicity).

---

## Block 2.5 — Samantha link to Feynman

| File | Type | Duration |
|---|---|---|
| E02-block02.5-samantha-link-to-feynman.mp3 | ElevenLabs / Samantha (Madeline) | 16s |

**Status:** COMPLETE ✅ — Audio 16s, clip trimmed to 16s in Premiere.

---

## Block 2.6 — AI-Feynman "you just ask them"

| File | Type | Duration |
|---|---|---|
| E02-block02.6-feynman.mp3 | ElevenLabs / Adam (American - New York) | 55s |

**Voice locked:** Adam - Confident, Clear and Direct (American - New York). Locked 2026-04-26.
**Status:** COMPLETE ✅ — Audio 55s, clip 54s, in Premiere.

---

## Block 2.7 — Samantha four-word payoff

| File | Type | Duration |
|---|---|---|
| E02-block02.7-samantha-four-word-payoff.mp3 | ElevenLabs / Samantha (Madeline) | 20s |

**Status:** COMPLETE ✅ — Audio 20s, clip trimmed in Premiere.

---

## Block 2.8 — Samantha 9-point summary (split into 3 parts)

Split into 3 × 3 points to keep Kling Avatar clips manageable. Old single-file E02-block02.8-samantha-9point-summary.mp3 superseded — do not use.

### Block 2.8a — Points 1–3

| File | Type | Duration |
|---|---|---|
| E02-block02.8a-samantha-points-1-3.mp3 | ElevenLabs / Samantha (Madeline) | 44s |

**Status:** COMPLETE ✅ — Audio 44s, clip 44s, in Premiere.

### Block 2.8b — Points 4–6

| File | Type | Duration |
|---|---|---|
| E02-block02.8b-samantha-points-4-6.mp3 | ElevenLabs / Samantha (Madeline) | 62s (1m02s) |

**Status:** COMPLETE ✅ — Audio 62s, clip 62s, in Premiere.

### Block 2.9 — Samantha bridge "Coming up"

| File | Type | Duration |
|---|---|---|
| E02-block02.9-samantha-coming-up.mp3 | ElevenLabs / Samantha (Madeline) | 10s |

**Status:** COMPLETE ✅ — Audio 10s, clip trimmed to 10s in Premiere.

---

### Block 2.8c — Points 7–9

| File | Type | Duration |
|---|---|---|
| E02-block02.8c-samantha-points-7-9.mp3 | ElevenLabs / Samantha (Madeline) | 46s |

**Status:** Audio ✅ 46s. Clip ✅ 47s raw (trim last ~0.5s in Premiere). Premiere: pending.
**Note:** Narration updated 2026-04-26 — "They came out of this stronger than ever" + "There is no trick for America to copy from China. China just found the hidden Achilles' heel of America."

---

## Block 3 — The Hive Pays You Back (mechanism animation)

| File | Type | Duration |
|---|---|---|
| E02-block03-hive-pays-you.mp3 | ElevenLabs / Samantha (Madeline) | 137s (2m17s) |

**Clips needed:** 23 shots × 6s = 138s (Kling 3.0 Omni, 720p, Native Audio OFF)

| Shot | File | Status |
|---|---|---|
| S1 | E02-block03-S1-joe-and-jane.mp4 | ✅ In Premiere |
| S2 | E02-block03-S2-private-vs-public.mp4 | ✅ In Premiere |
| S3a | E02-block03-S3a-hotel-reviews.mp4 | ✅ In Premiere |
| S3b | E02-block03-S3b-reviews-sorted.mp4 | ✅ In Premiere |
| S4 | E02-block03-S4-factory-catalogs.mp4 | ✅ In Premiere |
| S5 | E02-block03-S5-qa-testing.mp4 | ✅ In Premiere |
| S6a | E02-block03-S6a-john-doe-trip.mp4 | ✅ In Premiere |
| S6b | E02-block03-S6b-plain-jane-birthday.mp4 | ✅ In Premiere |
| S7a | E02-block03-S7a-no-datacenter-no-sub.mp4 | ✅ In Premiere |
| S7b | E02-block03-S7b-dream-vs-nightmare.mp4 | ✅ In Premiere |
| S8 | E02-block03-S8-bigai-vs-hive.mp4 | ✅ In Premiere |
| S9a | E02-block03-S9a-sleeping-homes.mp4 | ✅ In Premiere |
| S9b | E02-block03-S9b-usa-map-zzz.mp4 | ✅ In Premiere |
| S10 | E02-block03-S10-family-sleeping.mp4 | ✅ In Premiere |
| S11 | E02-block03-S11-crypto-no-hive-yes.mp4 | ✅ In Premiere |
| S12 | E02-block03-S12-staircase.mp4 | ✅ In Premiere |
| S13 | E02-block03-S13-climb-staircase.mp4 | ✅ In Premiere |
| S14 | E02-block03-S14-china-hammer.mp4 | ✅ In Premiere |
| S15 | E02-block03-S15-china-finances.mp4 | ✅ In Premiere |
| S16 | E02-block03-S16-laptops-light-up.mp4 | ✅ In Premiere |
| S17 | E02-block03-S17-china-buries-bigtech.mp4 | ✅ In Premiere |
| S18 | E02-block03-S18-tombstones.mp4 | ✅ In Premiere |
| S19 | E02-block03-S19-wilted-flower.mp4 | ✅ In Premiere |

**Status:** COMPLETE ✅ — Audio + all 23 clips in Premiere.

---

## Block 4 — No internet needed (the insurance racket)

| File | Type | Duration | Status |
|---|---|---|---|
| E02-block04-no-internet-insurance.mp3 | ElevenLabs / Samantha (Madeline) | 90s | ✅ In Premiere |
| E02-block04-S1a-internet-snaps.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S1b-money-drains.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S2-insurance-rejected.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S3-china-free-gift.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S4a-fishing-boat-cable.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S4b-ransomware-spares-china.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S4c-ddos-wave.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S5a-kid-throws-rock.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S5b-glazier-grins.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S6a-companies-migrate.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S6b-hive-grows-bigai-shrinks.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S6c-ceo-too-late.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S7a-ukraine-playbook.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S7b-china-same-playbook.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block04-S7c-bigtech-topples.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |

**Status:** COMPLETE ✅ — Audio + all 15 clips in Premiere.

---

## Block 5 — Every branch gets full attention (chess metaphor)

| File | Type | Duration | Status |
|---|---|---|---|
| E02-block05-every-branch.mp3 | ElevenLabs / Samantha (Madeline) | 40s | ✅ In Premiere |
| E02-block05-S1-chess-alone.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block05-S2-miss-the-rest.mp4 | Kling 3.0 Omni | 6s | ✅ In Premiere |
| E02-block05-S3-helpers-booths.mp4 | Kling 3.0 Omni | 6s | ⏳ Pending |
| E02-block05-S4-pick-winner.mp4 | Kling 3.0 Omni | 6s | ⏳ Pending |
| E02-block05-S5-next-turn.mp4 | Kling 3.0 Omni | 6s | ⏳ Pending |
| E02-block05-S6-alphago-move37.mp4 | Kling 3.0 Omni | 6s | ⏳ Pending |
| E02-block05-S7-hive-towers.mp4 | Kling 3.0 Omni | 6s | ⏳ Pending |

**Status:** Audio ✅ 40s. Shot plan ✅ (`BEESTING_2_BLOCK_5_SHOT_PLAN.md`). 2/7 clips done. Next: S3.
