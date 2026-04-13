# Part 1 / 14 — Hive Drones — Elements and Continuity

Reference-image library ("elements") and shot-to-shot continuity notes for Part 1. **All elements must be generated BEFORE any video clip in `PART_1_SHOT_LIST.md`.** This follows the Honeymation pre-production rule — lock the look of every recurring character, prop, and environment as a reference image first, THEN start generating clips. Doing it the other way produced 15 different-looking Architects in the first Honeymation pass and had to be thrown out.

---

## Two types of image assets — do not confuse them

### Elements (reference images)

- **What they are:** still images of recurring characters, props, and environments that appear in more than one shot.
- **How they are made:** OpenArt AI → Image mode → ChatGPT Image 1.5 → 1:1 1024×1024 → Medium quality → 4 variants → pick the best one → save to `elements/` folder in the repo.
- **How they are used:** uploaded into Kling 3.0 Omni video clips as **reference images** (NEVER as "start frame" — this is the same rule from the Honeymation pipeline). Kling uses them to understand what the character or prop should look like in the new clip.
- **Why they matter:** a character that appears in three shots must look identical in all three. Without a locked reference image, Kling will render a slightly different person every time and the series loses credibility the moment the viewer notices. The anchor of Shot 1 and the anchor of Shot 34 must be the same woman — if they look like two different people, the whole news-broadcast illusion breaks.

### Begin-frame / End-frame (continuity frames)

- **What they are:** specific still frames used to anchor where a shot starts and where it lands.
- **NOT elements.** They are shot-specific, not library items.
- **How they are used:** in Kling Video mode as "first frame" or "last frame" image conditioning. You give Kling the first frame and the last frame of a clip and it interpolates the motion between them. This is how you get two consecutive shots to feel like one unbroken piece of a single continuous event.
- **When to use them:** only when two consecutive shots have a continuity relationship — same character in the same space seconds apart, or one continuous motion cut into two beats. Most shots in Part 1 do NOT need them. The specific sequences that DO are listed below.

---

## Element library — Part 1

### Character elements

| # | Element | Description | Used in shots | Lock scope |
|---|---|---|---|---|
| 1 | **The anchor** | Female, mid-30s, dark navy suit, professional news-anchor hair, photorealistic, serious-urgent expression, sitting at a news desk. The face the entire series hangs on. | 1, 13, 34 | Series-wide (all 14 episodes) |
| 2 | **The reporter** | Male, mid-40s, trench coat, grounded field-reporter look, holding a non-branded microphone. | 15, 16, 24 | Series-wide (every episode has a reporter beat) |
| 3 | **The American boxer** | Athletic build, dignified professional expression, red/white/blue boxing shorts, standard boxing gloves, mouth guard, classic boxer stance. LOCKED LOOK per `FIGHT_METAPHOR_RULES.md` Rule 1. | 9, 19, 29 | Series-wide (all 14 episodes) |
| 4 | **The Part 1 Chinese Wing Chun fighter** | Athletic build, calm focused expression, plain black tang-style shirt and loose black pants, empty hands, Wing Chun ready stance. Per `FIGHT_METAPHOR_RULES.md` Rule 4 Part 1 style. | 9, 19, 29 | Part 1 only (each later episode has a different style so a new fighter element is generated) |
| 5 | **FBI agent's gloved hand** | Partial character — gloved hand holding a ballpoint pen, for the clipboard shots. Lock glove style and pen style so both drawings look like they came from the same hand. | 17, 21 | Part 1 only |
| 6 | **American generals (cold open climax)** | 3-4 US military officers in dress uniform at a conference table, horrified expressions. | 12 | One-shot usage |

**Nir Strulovitz portrait** is deliberately NOT an element — Shot 32 uses a phone-screen-showing-GitHub approach instead, which is production-friendlier and sidesteps any likeness rendering issues.

### Environment elements

| # | Element | Description | Used in shots | Lock scope |
|---|---|---|---|---|
| 8 | **News studio + desk** | Photorealistic modern news desk, clean emergency-broadcast key lighting, slightly cool color grade, neutral backdrop. No network logo, no ticker, no bug. | 1, 13, 34 | Series-wide |
| 9 | **Exterior bunker entrance** | Hardened American military bunker at the base of a mountain, heavy blast doors, warning signs, guard posts. | 5 (dawn), 15, 16, 24 (night with FBI vehicles) | Part 1 only |
| 10 | **Interior bunker hallway** | Metal walls, dim emergency red lighting, industrial feel. | 6, 8, 10, 11, 27, 28 | Part 1 only |
| 11 | **Industrial ventilation shaft** | Metal shaft with ventilation grate, dimly lit, drones entering. | 7 | One-shot usage |
| 12 | **Bunker sub-level conference room** | Dim conference table, emergency lighting. | 12 | One-shot usage |
| 13 | **California data center** | Photorealistic industrial building, rows of HVAC units on the roof, dawn light. | 18 (intact), 20 (burning) | Part 1 — may reappear in later episodes |
| 14 | **Pentagon war room** | Rows of monitor screens, American military officers in uniform. | 26 | One-shot usage |
| 15 | **Fight space** | Dim minimalist space, neutral background, cinematic photorealistic lighting. NOT a dojo (no kung-fu-movie clichés), NOT a boxing ring (no sports-entertainment), NOT a street (no found-footage). An empty warehouse-like space or cinematic void. | 9, 19, 29 | Series-wide (all 14 episodes) |

### Prop elements

| # | Element | Description | Used in shots | Lock scope |
|---|---|---|---|---|
| 16 | **Ballistic missile** | Chinese ballistic missile, photorealistic, dark grey, with a nose-cone that opens to release drones. | 2, 3, 4 | Part 1 only |
| 17 | **Worker drone** | Small quadcopter-style drone, matte black, autonomous look, no visible operator markings. **The visual identity of the whole swarm hangs on this one element.** | 3, 5, 7, 8, 10, 11, 23, 28 | Series-wide (will reappear in later episodes) |
| 18 | **Backup queen drone** | **Do NOT generate a separate element.** Per `ARCHITECTURE_NOTES.md` Rule 1, all drones look IDENTICAL from outside — queens cannot be distinguished from workers visually. Reuse Element #17 (Worker drone) for Shot 28's reveal. The reveal is in BEHAVIOR (the drone starts commanding others), not in appearance. | 28 | Reuses #17 |
| 19 | **FBI clipboard + paper + pen** | Legal-pad style paper on a clipboard, ballpoint pen. | 17, 21 | Part 1 only |
| 20 | **Raspberry Pi + small drone (scale shot)** | Photorealistic Raspberry Pi single-board computer held in an open human palm, next to a small drone for scale. Soft indoor lighting. | 31 | One-shot usage |
| 21 | **Phone showing GitHub page** | Photorealistic smartphone displaying the `strulovitz/MadHoney` GitHub repository page. | 32, 33 | Series-wide (every episode's closing shot references the book) |
| 22 | **Classified US military document with WRONG TOPOLOGY stamp** | Photorealistic printed document labeled "U.S. MILITARY AI ARCHITECTURE — CLASSIFIED" showing a star topology, with a red rubber stamp "WRONG TOPOLOGY" slammed on it. | 30 | One-shot usage |

### Graphic elements (designed in post, NOT generated as OpenArt images)

| # | Element | Where it lives | Used in |
|---|---|---|---|
| 23 | **BREAKING banner** | Adobe Premiere / Photoshop | Cold open (Shots 1, 13) |
| 24 | **`1 MONTH FROM NOW` chyron** | Adobe Premiere / Photoshop | Cold open (Shots 1, 13) |
| 25 | **End card layout** (slogan + part number + channel + book link + CTA) | Adobe Premiere / Photoshop | Shot 35 |

These three are locked in terms of style (sober sans-serif, dark background, white text hierarchy, no glow, no cartoon, no animation) but they are built at assembly time, not pre-generated as elements.

---

## Continuity notes — shot-to-shot frame linking

Most shots do NOT need begin-frame/end-frame conditioning. The sequences that DO are listed below. For these, the first frame of the second shot should visually match (or closely approximate) the last frame of the first shot.

### Continuity A — Missile flight (Shots 2 → 3 → 4)

Three beats of one continuous missile flight across the Pacific, opening mid-flight, then crashing empty.

- **Shot 2 end-frame ≈ Shot 3 begin-frame** — missile in mid-Pacific, nose-cone still closed, silhouette against dawn sky.
- **Shot 3 end-frame ≈ Shot 4 begin-frame** — empty missile body post-release, drones gone from frame, body now descending toward the mountain.

**Production tip:** generate Shot 3 FIRST (the nose-cone opening is the most distinctive beat), then use its first frame as Shot 2's end-frame reference and its last frame as Shot 4's begin-frame reference. Build the sequence backwards from the most distinctive beat.

### Continuity B — Drones entering the bunker (Shot 7 → Shot 8)

Same drones, same bunker interior, seconds apart in real time.

- **Shot 7 end-frame ≈ Shot 8 begin-frame** — drones exiting the ventilation grate into the bunker hallway and approaching the locked door.

### Continuity C — FBI clipboard drawings (Shot 17 → Shot 21)

Same clipboard, same hand, same pen. Shot 18 (star dissolving to data center) sits between them but is a cross-dissolve, not a continuity cut.

- **Shot 17 end-frame** = completed star drawing on the top half of the paper.
- **Shot 21 begin-frame** = same clipboard, same paper, hand moving to the bottom half (or a fresh area) to draw the tree.

The two drawings must look like they happened in one real sitting on the same clipboard, not on two different pieces of paper.

### Continuity D — The fight across the three cutaways (Shots 9 → 19 → 29)

**The most important continuity sequence in Part 1.** The three fight cutaways must feel like three beats of the **same ongoing fight** — same fighters, same space, same fight progressing — not three separate fights.

- **Shot 9 → Shot 19:** boxer was fresh and upright in Shot 9. In Shot 19 he is slightly winded, the trap is the escalation from the missed hook. The body language progresses; the wardrobe and injuries do not. Per `FIGHT_METAPHOR_RULES.md` Rule 2 — NO cumulative damage, both fighters start each episode fresh and healthy. The escalation is in BREATHING and BODY LANGUAGE only. No bruises, no blood, no broken nose.
- **Shot 19 → Shot 29:** boxer's arm was trapped in Shot 19. In Shot 29 he is now breathing hard, professional recognition on his face as he realizes he cannot land a hit. Still no visible injuries.
- **Shot 9 end-frame ≈ Shot 19 begin-frame** — boxer's fist sailing through empty air, fighter stepping aside into the trap position.
- **Shot 19 end-frame ≈ Shot 29 begin-frame** — boxer being released from the trap, starting to throw the cross, fighter already beginning to drop low.

All three cutaways reuse Element #15 (fight space), Element #3 (boxer), and Element #4 (Wing Chun fighter). Same lighting, same wardrobe, same fighters throughout.

### Continuity E — The bunker battle turn (Shot 27 → Shot 28)

Shot 27 shows soldiers killing one queen drone, believing they have won. Shot 28 reveals the backup queen was already flying elsewhere in the bunker. Same battle, same bunker, different corner.

- **Shot 27 end-frame → Shot 28 begin-frame** — lighting, atmosphere, and grim mood carry over. The two shots are in different rooms of the same bunker but the tonal grade must be continuous. Not a strict frame-for-frame match, but the color temperature and emergency-lighting feel must be identical.

### Continuity F — The closing tonal run (Shots 31 → 32 → 33 → 34 → 35)

Not a frame-level continuity (each beat is a different subject) but all five shots should share the same "quiet, serious, late-night broadcast" tonal grade. The anchor's face in Shot 34 should look like the same broadcast the cold open started in, just hours later and more grave.

---

## Elements generation order (strict priority, before any video clip)

Generate every element as a locked reference image BEFORE starting any video clip. Within that, the priority order is:

1. **The anchor (#1)** — she opens and closes the video, must be locked first. Shots 1 and 34 are the most important lip-sync shots of the episode and everything else depends on her.
2. **The worker drone (#17)** — appears in 8 shots, any inconsistency is instantly visible to the viewer. Series-wide reuse.
3. **The American boxer (#3)** — series-wide lock, reused in all 14 episodes.
4. **The Wing Chun fighter (#4)** — Part 1 specific, locks the opponent for this episode.
5. **The fight space (#15)** — series-wide lock, reused in all 14 episodes for the cutaways.
6. **The news studio + desk (#8)** — locks the news-broadcast frame.
7. **The reporter (#2)** — locks the Act 2 first half look.
8. **The exterior bunker entrance (#9)** and **interior bunker hallway (#10)** — lock the attack location.
9. **The ballistic missile (#16)** — locks the cold-open vehicle.
10. **The FBI clipboard + hand + pen (#5 + #19)** — locks the topology explanation beat.
11. **Remaining one-shot usage elements (#6, #11, #12, #13, #14, #20, #21, #22)** — generate as needed during production, no priority.

Graphic elements (#23, #24, #25) are designed at assembly time in Adobe Premiere Pro or Photoshop, not generated in OpenArt.

---

## Status tracker

| # | Element | Type | Used in shots | Priority | Status |
|---|---|---|---|---|---|
| 1 | The anchor | Character | 1, 13, 34 | 1 | LOCKED → `elements/01_anchor.png` |
| 2 | The reporter | Character | 15, 16, 24 | 7 | LOCKED → `elements/02_reporter.png` |
| 3 | American boxer | Character | 9, 19, 29 | 3 | LOCKED → `elements/03_american_boxer.png` |
| 4 | Wing Chun fighter (Part 1) | Character | 9, 19, 29 | 4 | LOCKED → `elements/04_wing_chun_fighter.png` |
| 5 | FBI agent's hand | Character (partial) | 17, 21 | 10 | TO DO |
| 6 | American generals | Character | 12 | 11 | TO DO |
| 8 | News studio + desk | Environment | 1, 13, 34 | 6 | LOCKED → `elements/08_news_studio.png` |
| 9 | Exterior bunker entrance | Environment | 5, 15, 16, 24 | 8 | LOCKED → `elements/09_bunker_exterior.png` |
| 10 | Interior bunker hallway | Environment | 6, 8, 10, 11, 27, 28 | 8 | TO DO |
| 11 | Industrial ventilation shaft | Environment | 7 | 11 | TO DO |
| 12 | Bunker sub-level conference room | Environment | 12 | 11 | TO DO |
| 13 | California data center | Environment | 18, 20 | 11 | TO DO |
| 14 | Pentagon war room | Environment | 26 | 11 | TO DO |
| 15 | Fight space (series-wide) | Environment | 9, 19, 29 | 5 | LOCKED → `elements/15_fight_space.png` |
| 16 | Ballistic missile | Prop | 2, 3, 4 | 9 | TO DO |
| 17 | Worker drone | Prop | 3, 5, 7, 8, 10, 11, 23, 28 | 2 | LOCKED → `elements/17_worker_drone.png` |
| 19 | FBI clipboard + paper + pen | Prop | 17, 21 | 10 | TO DO |
| 20 | Raspberry Pi + small drone | Prop | 31 | 11 | TO DO |
| 21 | Phone showing GitHub page | Prop | 32, 33 | 11 | TO DO |
| 22 | Classified document w/ WRONG TOPOLOGY stamp | Prop | 30 | 11 | TO DO |

Update this table as each element is locked. Status options: `TO DO` → `GENERATING` → `LOCKED` → file path to the saved reference image.

---

## Next step

Claude will produce the OpenArt Image prompt for **Element #1 — the anchor** first, following the Honeymation reference-image workflow: OpenArt AI → Image mode → ChatGPT Image 1.5 → 1:1 1024×1024 → Medium quality → 4 variants. She must be locked before any video clip or lip-sync avatar generation can begin. Ask for it when ready.
