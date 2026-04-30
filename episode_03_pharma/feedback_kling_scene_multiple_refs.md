---
name: Kling scene workflow = prototype portrait → meta-reference → scene refs → Kling
description: For any BeeSting scene with a human, FIRST generate a prototype portrait of the character, THEN upload that prototype as an attached image-reference inside ChatGPT Image to generate scene-specific refs. Kling has zero memory; ChatGPT Image generates each text prompt fresh; identical text alone does NOT lock a face. Only an attached image reference does.
type: feedback
originSessionId: 4f771034-6bdb-44f4-8ad7-0939e0116ea6
---
A BeeSting "scene" with a human character requires this exact four-step workflow. Both Kling and ChatGPT Image have zero memory between prompts. Saying "the same woman" or "use the same character" in pure text is meaningless — these are stateless generators that only see what is **physically attached** to the current prompt.

## THE FAILURE MODES (do not repeat)

1. **Single detail-only reference** (e.g. "just a hand and a cabinet"): Kling has no character to lock onto and invents a different woman every frame. Wasted credits.
2. **Multiple scene images with byte-identical character text but no prototype**: ChatGPT Image generates three differently-faced women because text alone cannot reproduce a specific face. Wasted credits.
3. **Telling Kling "the same as the previous clip"**: Kling has zero memory of previous clips. It only sees what is uploaded into the current reference slot. Wasted credits.

## THE CORRECT WORKFLOW

### STEP 0 — PROTOTYPE PORTRAIT
Generate ONE ChatGPT Image with **text only** (no attached reference). This is the canonical visual definition of the character — the "meta-reference."
- Clean portrait, neutral or minimal background, no scene context
- Face clearly visible, full upper body or three-quarter
- All clothing, hair, defining features visible
- Include at least one **specific recognizable detail** (a mole, a freckle pattern, a scar, an asymmetric feature) that gives ChatGPT Image something concrete to lock onto in later passes
- Direct neutral pose, neutral expression
- Save as `gpt_image_prompt_0_prototype.txt` in Downloads

### STEP 1, 2, 3 — SCENE REFERENCE IMAGES
For EACH scene image, the user **uploads the prototype PNG into ChatGPT Image as an attached image-reference**, alongside the text prompt. Each scene text prompt:
- **Begins with**: "Use the woman in the attached reference image."
- Explicitly instructs ChatGPT Image to keep her exact face, hair, clothing, defining features from the attached prototype — say "do not change her face, do not change her clothing"
- Then describes the new environment, action, pose, expression for that scene moment
- Saves as `gpt_image_prompt_1_<state>.txt`, `gpt_image_prompt_2_<state>.txt`, `gpt_image_prompt_3_<state>.txt`

Result: 3 scene images with the same woman because all three are generated from the same uploaded prototype.

### STEP 4 — KLING
Upload the 3 **scene reference images** (NOT the prototype) into Kling 3.0 as the reference slots for ONE clip. Kling 3.0, 16:9, Pro, reference mode, Native Audio OFF.
- Kling animates the motion described in the Kling prompt
- Kling locks character identity to what it sees in the 3 attached references
- Because the 3 references show the same woman (because they were all generated from the same prototype), Kling renders the same woman across the clip

## WHY THIS WORKS AND TEXT-ALONE DOES NOT

- Kling has zero memory across prompts. "Same as before," "the same woman," "consistent character" — all meaningless without an attached reference image. Kling only sees what is physically uploaded to the current prompt.
- ChatGPT Image text-only generation cannot reproduce a specific face from a verbal description. Two prompts with identical text produce two different faces. The visual seed is not deterministic enough.
- Only an **attached image reference** inside ChatGPT Image fixes the face.
- The prototype is the load-bearing artifact. Every scene image is generated FROM the prototype.

## RULES FOR FUTURE SESSIONS

- Always start with a prototype prompt before writing any scene prompts.
- Number prototype as `0_prototype`, scenes as `1_`, `2_`, `3_`, etc.
- In every scene prompt, the FIRST sentence must be "Use the woman in the attached reference image."
- Never tell Kling or ChatGPT Image "the same as before" without an attached reference.
- Never give Kling a single detail-only reference for a scene with a human character.
- This rule is universal across every BeeSting video, every project, every character.
