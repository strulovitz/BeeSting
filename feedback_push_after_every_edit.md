---
name: push to GitHub after every file edit
description: After ANY file edit/create that affects a tracked repo (prompts, scripts, memory files, transcripts, plans), immediately copy to the appropriate repo, commit, and push. Do not batch.
type: feedback
originSessionId: 4f771034-6bdb-44f4-8ad7-0939e0116ea6
---
After **every** file edit or create that affects a project — whether it's a ChatGPT Image prompt, a Kling prompt, a shot plan, a memory file, a conversation transcript, a settings change, anything — **immediately commit and push to GitHub**. Do not batch multiple edits into one push. Do not wait until "the end of the session."

**Why:** Nir said on 2026-04-30 — "push to github each time fucking scum." He has been burned repeatedly by sessions that died, machines that crashed, and Claude sessions that lost work because the artifact was only on disk and never on GitHub. Every uncommitted edit is one outage away from being lost. Per `feedback_save_everything.md`: nothing is real until it is on GitHub.

**How to apply:**

1. **Edit the file once** (the source of truth — usually in Downloads for prompts, or in `~/.claude/projects/.../memory/` for memories).
2. **Immediately copy it to the appropriate repo location.** For BeeSting work that means `BeeSting/episode_<n>_<topic>/`. For repo-specific memories, the repo's own folder.
3. **Immediately `git add` + `git commit` + `git push`** in a single sequential operation.
4. **Confirm to Nir in chat** with the commit hash and the GitHub link in one short line.
5. **One edit, one push.** Do not stack multiple edits before pushing — each edit gets its own commit.

This applies to:
- ChatGPT Image prompts (`gpt_image_prompt_*.txt`)
- Kling prompts (`kling_prompt*.txt`)
- ElevenLabs prompts (`elevenlabs_prompt*.txt`)
- Shot plans (`*_SHOT_PLAN.md`)
- Memory files (any `feedback_*.md`, `project_*.md`, etc.)
- Conversation transcripts
- Any other artifact Claude produces in a session

**Exceptions:** none. If Nir explicitly says "do not push yet," wait. Otherwise, push every time.

**The mental model:** treat every file as if Claude is about to die in the next 30 seconds. The only thing that survives is what is on GitHub.
