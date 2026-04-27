# Where We Stopped — 2026-04-27

## What is DONE

- **Block 3 COMPLETE** — all 23 clips in Premiere, audio in Premiere.
- **Block 4 COMPLETE** — all 15 clips in Premiere, audio in Premiere. Full shot plan lives in `BEESTING_2_BLOCK_4_SHOT_PLAN.md`.
- **Block 5 narration DONE** — file `audio/E02-block05-every-branch.mp3` (40 seconds, Samantha / Madeline). Already in Premiere.

## What to do next — FOR OPUS 4.7 (PLANNER)

Block 5 needs a full detailed shot plan before any clips are generated.

### The problem with the current Block 5 skeleton

`BEESTING_2.md` has a 4-shot skeleton for Block 5. **This is not enough.**

- Narration: 40 seconds
- 40 ÷ 6 = 6.7 → **7 clips needed minimum**
- Current skeleton: only 4 shots × 6s = 24s — covers barely half the narration

Opus 4.7 must expand the shot plan from 4 shots to 7 shots, then write the full detailed plan into a new file `BEESTING_2_BLOCK_5_SHOT_PLAN.md`, following the exact same format as `BEESTING_2_BLOCK_4_SHOT_PLAN.md`.

### What the plan file must contain (same structure as Block 4)

- Locked production rules section (Kling settings, palette, no-text-animation rule, etc.)
- The full narration text broken into per-shot lines
- A detailed prose description of each of the 7 clips: reference-image content, palette, animation behaviour, camera move
- Continuity notes between clips
- Camera variety check (no two consecutive clips with same move)
- Step-by-step handoff procedure for the Sonnet executor session

### The narration (40s, already locked in BEESTING_2.md Block 5.1)

> *"Point three. Every branch gets full attention."*
>
> *"Imagine playing chess alone. Too many moves, too little time. You think about a few. You miss the rest."*
>
> *"With helpers — one per piece — every move gets thought about at the same time."*
>
> *"Each helper returns with their best move. You pick the winner. The updated board goes back to all the helpers. Next turn, same thing."*
>
> *"This is how AlphaGo beat the human world champion at Go with Move 37 — a move no human would have played. But AlphaGo was still one giant computer. The Hive, running on half a billion computers, misses nothing at all."*

### The 4-shot skeleton to expand (from BEESTING_2.md)

| Shot | Visual |
|---|---|
| S1 | Stressed human alone at chess board, chaotic pieces spinning above head, clock at zero |
| S2 | Six helpers in booths, one piece type each, all thinking in parallel |
| S3 | Helpers return best moves, player picks winner, updated board loops back to all helpers with NEXT TURN arrow |
| S4 | Chess board transitions to Go board. Three-tier hierarchy: Human (small) → AlphaGo (medium, MOVE 37) → Hive pyramid (huge, HALF A BILLION COMPUTERS · MISSES NOTHING) |

Opus 4.7 must decide where to add the 3 extra shots so the narration is fully covered with no dead air. The narration lines must map 1:1 to shots.

### Palette and style

- **Palette:** deep burgundy + gold + cream — royal chess-club aesthetic
- **Style:** Kurzgesagt flat 2D, same family as Blocks 3 and 4
- Key framing lock (Nir 2026-04-24): **Human < AlphaGo < Hive** — do NOT conflate AlphaGo with the Hive. AlphaGo was one giant centralized computer. The Hive does not prune at all.

### After Opus 4.7 writes the plan

Sonnet 4.6 executes it clip by clip following the same one-clip-at-a-time workflow as Block 4:
ChatGPT Image prompt → download PNG → rename/copy → read image → Kling prompt → download MP4 → rename/copy → commit/push → drag into Premiere → next clip.

## Production rules — quick recap

- Kling 3.0 Omni, 720p (NEVER Pro), Native Audio OFF, 6 seconds per clip, reference image mode
- Never ask Kling to animate text — text must already be drawn into the reference image, frozen
- No graphs, no charts, no numeric counters that update over time
- Reference image must show the FINISHED state — Kling animates it, does not build it
- Camera angle must vary every clip
- One clip at a time — write ChatGPT Image prompt, generate, process, write Kling prompt, generate, process, commit, drag into Premiere, only then move to the next clip
- Never name OpenAI / Google / Anthropic / xAI / ChatGPT / Claude / Gemini / Grok — use "Big AI" / "Big Tech"
