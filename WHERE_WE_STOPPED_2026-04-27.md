# Where We Stopped — 2026-04-27

## What is DONE

- **Block 3 COMPLETE** — all 23 clips in Premiere, audio in Premiere.
- **Block 4 COMPLETE** — all 15 clips in Premiere, audio in Premiere.
- **Block 5 COMPLETE** — all 7 clips in Premiere, audio in Premiere. Shot plan in `BEESTING_2_BLOCK_5_SHOT_PLAN.md`.

## 🚨 CRITICAL LESSON FROM BLOCK 5 — READ BEFORE WRITING ANY KLING PROMPT 🚨

Block 5 Kling prompts were lazy and produced static-looking clips. One clip (S7) drifted from the visual style entirely because the style was never stated in the prompt. Full details and the correct template are in `KLING_PROMPT_LESSONS.md`. Read it before writing a single Kling prompt.

**Summary:** Every Kling prompt must have: (1) visual style, (2) scene context, (3) animation action, (4) camera move. Minimal prompts are the EXCEPTION for broken reference images only — NOT the standard.

## What to do next

**Block 6 — Mechanism cashing Point 4: Snowden diagnosed, the Hive cures.**

- Audio not yet generated
- Palette: dark slate grey + red ink + cream — surveillance / paper-trail vibe
- ~27s narration, 3 base shots in skeleton
- Script in `BEESTING_2.md` Block 6.1
- **Math check:** 27s ÷ 6 = 4.5 → need at least 5 clips. The 3-shot skeleton in `BEESTING_2.md` is too short. **Opus 4.7 must write a proper shot plan first** (same as Block 4 and Block 5) before any clips are generated.

### Step 1 — Opus 4.7 writes the shot plan
Read `BEESTING_2.md` Block 6, count the narration words, divide by 6, plan that many shots. Write the full plan to `BEESTING_2_BLOCK_6_SHOT_PLAN.md` following the format of `BEESTING_2_BLOCK_4_SHOT_PLAN.md` and `BEESTING_2_BLOCK_5_SHOT_PLAN.md`.

### Step 2 — Generate narration audio
ElevenLabs, Samantha (Madeline – Professional Narrator), narration text from `BEESTING_2.md` Block 6.1.

### Step 3 — Sonnet 4.6 executes clip by clip
Follow the shot plan. Use FULL Kling prompts per `KLING_PROMPT_LESSONS.md`.

## Production rules — quick recap

- Kling 3.0 Omni, 720p (NEVER Pro), Native Audio OFF, 6 seconds per clip, reference image mode
- Never ask Kling to animate text — text must already be drawn into the reference image, frozen
- Reference image must show the FINISHED state
- Camera angle must vary every clip
- One clip at a time
- Never name OpenAI / Google / Anthropic / xAI / ChatGPT / Claude / Gemini / Grok
- **FULL Kling prompts always** — see `KLING_PROMPT_LESSONS.md`
