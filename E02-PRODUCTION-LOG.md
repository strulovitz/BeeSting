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

**Status:** Audio ✅ 20s. Clip ✅ 20s (Kling Avatar, trim last ~0.5s in Premiere). Premiere: pending.
**Note:** Narration updated 2026-04-26 — "They came out of this stronger than ever" + "There is no trick for America to copy from China. China just found the hidden Achilles' heel of America."

---
