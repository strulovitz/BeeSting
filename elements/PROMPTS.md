# BeeSting — Element Generation Prompts

Every OpenArt Image prompt used to generate the reference images in `BeeSting/elements/`, saved verbatim. Any future session can regenerate the exact same look by copy-pasting the prompts below into OpenArt. This file follows Nir's standing rule: **save EVERY prompt/setting/decision to the repo, never rely on conversation history or Claude's memory.**

Prompts are listed in the order they were generated (NOT by element number) so the file reads like a production log.

---

## Standard OpenArt settings (same for every element unless explicitly noted)

- **Tool:** `openart.ai/generator/lego` → **Image** mode
- **Model:** ChatGPT Image 1.5
- **Proportions:** 1:1 (1024×1024)
- **Quality:** Medium
- **Number of images:** 4
- **Omni Reference:** noted per element (most are empty; some reuse an earlier locked element)

---

## Series-wide locked rules that apply to every element prompt

From `VISUAL_HOOK_RULES.md` Rule 4 and `FIGHT_METAPHOR_RULES.md`:

- **Photorealistic only.** NEVER Lego, NEVER Pixar, NEVER comics, NEVER anime, NEVER cartoon, NEVER body-cam, NEVER video-game render. Every prompt ends with some variant of the line *"Not stylized. Not cartoon. Not Pixar. Not anime. Not illustrated."* — do not remove it.
- **No network logos, no branding, no text, no flags** in the background of any studio or environment shot. The generic uncanny feel is the whole hook of the series.
- **No stereotypes** for the Chinese fighter — modern grounded look, no queue, no Fu Manchu, no Chinatown clichés. Per Rule 4 of `FIGHT_METAPHOR_RULES.md`.
- **The American boxer is sympathetic, dignified, professional.** NEVER a clown, NEVER a brute. Per Rule 1 of `FIGHT_METAPHOR_RULES.md`.

## Anti-crop framing rule

For full-body character shots, OpenArt sometimes crops at the head and feet. Two fallback strategies in priority order:

1. **Natural photography vocabulary first** — *"full-length portrait photograph, wide shot, entire body in frame from the top of his head to the soles of his boxing boots on the ground"*. Preferred because it does not create weird empty strips.
2. **Honeymation anti-crop template as fallback** — verbatim: *"Full body visible from top of head to bottom of feet. Character takes up about X% of the image height. Lots of empty space above and below."* Start at 70%, drop to 60% if cropping persists, 50% as a last resort. The tradeoff: creates visible empty space above and below the subject, which must be cropped in Premiere during assembly.
3. **Only use the fallback when natural framing has already failed.** The anchor (chest-up), the reporter (chest-up), the studio (environment), and the fight space (environment) did not need the anti-crop template. The boxer required it after natural framing failed — we ended up at 60%.

---

## Element #1 — The Anchor

- **Status:** LOCKED → `elements/01_anchor.png`
- **Omni Reference:** none (first element generated)
- **Used in shots:** 1, 13, 34
- **Scope:** Series-wide lock, reused in all 14 episodes. She is the face of the whole series. This reference image is also the source for Kling Avatar lip-sync generation on Shots 1 and 34.

```
Photorealistic female news anchor, mid-30s, chest-up framing as if shot by a studio broadcast camera. She is sitting behind a modern dark news desk. She wears a sharply tailored dark navy blazer over a simple dark top, small minimal earrings, subtle professional makeup, and her hair is styled in a conservative shoulder-length news-anchor look — neat, not overly styled. Her expression is serious, urgent, composed — a professional delivering breaking news, not smiling, not panicking. She looks directly into the camera lens with full eye contact.

The studio lighting is clean cool-toned key light from slightly above and in front of her, giving her a crisp well-lit appearance with soft natural shadows. The background behind her is a neutral modern news-studio backdrop in dark grey or deep navy, slightly out of focus with a shallow depth of field. No network logo. No LED wall. No ticker. No text. No graphics of any kind. No nameplate on the desk. No visible microphone on the desk — the microphone is a concealed lapel mic. Clean and sober.

Photorealistic, shot on a professional broadcast camera, the look of real network news — think CNN, Fox News, BBC World, i24, Al Jazeera English. Real human face, real fabric, real skin texture, real studio lighting. This is what a viewer would see if they turned on their television tonight and their network cut into programming with a breaking news alert.

Not stylized. Not cartoon. Not Pixar. Not anime. Not illustrated. Not glossy. Not exaggerated. Just a real professional news anchor in a real news studio.

1:1 square aspect ratio.
```

---

## Element #17 — Worker Drone

- **Status:** LOCKED → `elements/17_worker_drone.png`
- **Omni Reference:** none
- **Used in shots:** 3, 5, 7, 8, 10, 11, 23, 28
- **Scope:** Series-wide (will likely reappear in Parts 2C DoD Maginot, Part 5 Defense Contractors, etc.)

```
Photorealistic single small military-grade quadcopter drone, matte black carbon-fiber body, four rotors with dark blades, compact utilitarian design about the size of a human hand. Aggressive autonomous combat look — not a consumer toy, not a hobby drone, not a big expensive military Predator. This is a cheap mass-produced combat drone of the kind that could be built in a Chinese factory by the millions. The body is angular and functional, no branding, no markings, no flag, no logo, no serial number visible. A small dark camera lens or sensor is visible on the front. Concealed internal compartment for whatever payload it carries. Landing skids or stubby legs underneath.

The drone is shown hovering in mid-air, slightly angled so the viewer sees the top and one side of the body clearly. Rotors are in motion with a soft motion blur. Lighting is clean neutral studio lighting from slightly above and in front, with soft shadows beneath — the drone is isolated on a plain dark grey or near-black background so it reads as a reference image that can be dropped into any later scene. No ground, no wall, no clutter behind it. Just the drone, clearly visible, photorealistic.

Think of it as an engineering reference photograph of a new Chinese military drone that has just been unveiled — the kind of still image that would appear on a defense news website, sober and unembellished, photographed to document the hardware accurately.

Photorealistic, real camera, real materials, real lighting. Not stylized. Not cartoon. Not Pixar. Not anime. Not illustrated. Not glossy CGI render. Just a real small black combat drone, shot like a real product photograph.

1:1 square aspect ratio.
```

---

## Element #3 — The American Boxer (FINAL — after three iterations)

- **Status:** LOCKED → `elements/03_american_boxer.png`
- **Omni Reference:** none
- **Used in shots:** 9, 19, 29 (all fight cutaways in Part 1), AND all fight cutaways in all 14 episodes
- **Scope:** Series-wide lock. Per `FIGHT_METAPHOR_RULES.md` Rule 1 his look never changes across episodes.

### Iteration history (what did NOT work — do not repeat these mistakes)

1. **First attempt (natural photography framing, no anti-crop template):** head and feet were cropped. Natural vocabulary alone was not enough.
2. **Second attempt (added 70% anti-crop template):** still cropped at head and feet but slightly better.
3. **Third attempt (dropped to 60% anti-crop template):** showed his eyes and most of his feet, but still cropped a little at top and bottom, and the mouth guard line *"black mouth guard visible between his lips"* made the model paint his lips black, creating a lipstick look.
4. **Fourth attempt (60% + mouth guard line removed entirely):** LOCKED. The boxer's mouth is closed in a calm focused expression instead, and the mouth guard can be added back into the Kling Video prompts for the fight cutaway clips where his mouth is open mid-punch.

### The locked prompt

```
Photorealistic professional male American boxer, mid-30s, athletic build, welterweight-to-middleweight physique, lean and powerful. Full body visible from top of head to bottom of feet. Character takes up about 60% of the image height. Lots of empty space above and below.

He is standing in a classic Western boxing stance, weight slightly forward, gloves raised in guard position, eyes focused and determined. His mouth is closed in a calm focused expression. His expression is serious, composed, courageous — a respected professional doing his craft, not a showman, not angry, not afraid. He looks like the kind of boxer you would be proud to watch fight on pay-per-view.

Wardrobe locked: red, white, and blue American flag boxing shorts (stars and stripes pattern), standard black professional boxing gloves, bare chest and defined shoulders and arms, ankle-high boxing boots. No name on the shorts, no sponsor logos, no title belts, no tattoos visible. Keep him clean and universal so he reads as "every American boxer," not any specific real person.

Plain dark grey or near-black background, slightly vignetted, studio-lit from slightly above and in front to catch the definition of his muscles and the sweat on his skin. No ring, no ropes, no crowd, no gym equipment — just the boxer isolated against a clean dark background.

Photorealistic, real camera, real skin texture, real fabric, real sweat, real lighting — the look of a professional fight-night promotional photograph. Not stylized. Not cartoon. Not Pixar. Not anime.

1:1 square aspect ratio.
```

### When generating the fight-cutaway video clips for this boxer

Add **"black mouth guard visible"** back into the Kling Video prompt for Shots 9, 19, and 29 — real boxers in action have the mouth guard visible, but the reference image has the mouth closed for rendering stability. This is the one detail that differs between the element reference and the action clips.

---

## Element #4 — The Part 1 Wing Chun Fighter

- **Status:** LOCKED → `elements/04_wing_chun_fighter.png`
- **Omni Reference:** none
- **Used in shots:** 9, 19, 29
- **Scope:** Part 1 only. Each later episode gets a different style (Snake/jian/Guandao/Tiger/Chain whip/Spear/Drunken Master/Tai Chi/Eagle Claw/Mantis/Nunchaku/Crane/final capstone) so a new fighter element is generated for each. Per `FIGHT_METAPHOR_RULES.md` Rule 4.

```
Photorealistic Chinese male Wing Chun kung fu master, mid-30s, athletic lean build, calm and focused expression. Full body visible from top of head to bottom of feet. Character takes up about 60% of the image height. Lots of empty space above and below.

He is standing in the classic Wing Chun ready stance — feet shoulder-width apart in a slight pigeon-toed triangle stance, knees slightly bent, weight centered low, both hands raised in front of his chest in the Wing Chun guard position (one hand forward, one hand back, both hands open and relaxed, ready to trap and redirect). His mouth is closed. His expression is calm, centered, observant — a disciplined professional who has trained for twenty years, not angry, not smiling, not theatrical. He looks like a respected modern kung fu master, the kind you would see in a real Foshan training hall today, not like an old Hong Kong movie caricature.

Wardrobe: plain traditional black tang-style shirt with a mandarin collar (short-sleeved or long-sleeved, solid black, no embroidery, no dragons, no gold trim), loose plain black cotton kung fu pants, plain black cloth kung fu shoes. No weapons in his hands — this is empty-hand Wing Chun. No props. No belts, no sashes, no headbands. Hair is modern short, neat, professional — NOT a queue, NOT a topknot, NOT long flowing hair. Clean-shaven face, no Fu Manchu mustache, no stereotyped facial hair of any kind.

Plain dark grey or near-black background, slightly vignetted, studio-lit from slightly above and in front. No dojo, no Chinese temple, no bamboo, no red lanterns, no calligraphy on the walls, no martial arts props — just the fighter isolated against a clean dark background so the image can be used as a reference for any later scene.

Photorealistic, real camera, real skin texture, real fabric, real studio lighting — the look of a modern professional portrait photograph of a real Wing Chun instructor, the kind that would appear in a documentary about Ip Man's lineage. Not stylized. Not cartoon. Not anime. Not a kung fu movie poster. Not old Hong Kong cinema. Grounded, modern, dignified.

1:1 square aspect ratio.
```

---

## Element #15 — The Fight Space

- **Status:** LOCKED → `elements/15_fight_space.png`
- **Omni Reference:** none
- **Used in shots:** 9, 19, 29 (all Part 1 cutaways), AND all fight cutaways in all 14 episodes
- **Scope:** Series-wide lock. Per `FIGHT_METAPHOR_RULES.md` Rule 4 — the same physical space across the entire series, so viewers recognize *"we are back in the fight space"* instantly.

```
Photorealistic empty industrial fighting space, interior of a large abandoned warehouse or empty loft, bare concrete floor, bare concrete or dark brick walls in the far background, high ceiling barely visible in shadow above. The space is completely empty — no boxing ring, no ropes, no crowd, no audience, no chairs, no training equipment, no punching bags, no weapons racks, no dojo mats, no temple decorations, no bamboo, no lanterns, no signs. Just a large open empty floor with bare walls receding into darkness.

The lighting is dramatic and cinematic but restrained — a single overhead key light from above casts a soft circular pool of light on the center of the floor, while the edges of the space fade into deep shadow and near-black darkness. The overall mood is quiet, ominous, suspended outside of time. A cold neutral color temperature, slightly desaturated, almost black-and-white but retaining just enough warmth that skin tones will look natural when a fighter is placed in the space.

Floor is bare polished concrete with visible texture and slight reflections of the overhead light. Walls in the far background are barely visible, suggested rather than shown, dark grey or near-black. No windows, no doors, no visible exits. The space feels like it could be anywhere on earth and nowhere in particular.

Photorealistic environment reference photograph, wide shot, empty frame ready for characters to be composited into the center, taken by a real camera with real lens, real cinematic lighting, real depth of field. Not stylized. Not cartoon. Not Pixar. Not anime. Not a video-game environment render. Just a real empty industrial space photographed in low moody light.

1:1 square aspect ratio.
```

---

## Element #8 — The News Studio + Desk

- **Status:** LOCKED → `elements/08_news_studio.png`
- **Omni Reference:** none
- **Used in shots:** 1, 13, 34
- **Scope:** Series-wide lock. Uploaded together with Element #1 (the anchor) when generating video clips, so Kling knows both what she looks like and what her studio environment looks like.

```
Photorealistic empty modern news broadcast studio, wide shot of the anchor's news desk and the backdrop behind it, no anchor in the frame — just the environment. The news desk is a modern sleek dark surface, glossy near-black or deep charcoal, smooth and minimalist, positioned in the center-foreground of the shot. No nameplate, no branded microphone, no papers, no props, no clutter on the desk — it is clean and empty.

The backdrop behind the desk is a neutral modern studio wall in dark grey or deep navy, slightly textured, slightly out of focus with a shallow depth of field. The backdrop is intentionally generic so it could pass for any major news network. Absolutely no network logo, no channel name, no LED screen, no video wall, no world map, no ticker text, no chyron graphics, no BREAKING banner, no call letters, no text of any kind anywhere in the frame.

Studio lighting is a clean cool-toned three-point setup — strong key light from slightly above and in front of where the anchor would sit, soft fill light on the opposite side, and a subtle rim light from behind to separate the desk and backdrop visually. The overall feel is professional emergency-broadcast lighting: a little cooler than warm, slightly desaturated, serious and sober, not glamorous.

Slight cinematic vignette around the edges of the frame. The composition leaves room in the center for a news anchor to be seated at the desk — the desk occupies the lower third, the backdrop fills the upper two-thirds, and there is an empty seat visible behind the desk where the anchor belongs.

Photorealistic, real studio camera, real lens, real cinematic depth of field. The look of a real network news studio between broadcasts — the kind of behind-the-scenes reference photograph a set designer would take to document the setup. Not stylized. Not cartoon. Not Pixar. Not anime. Not a video-game environment render. Just a real empty professional news studio.

1:1 square aspect ratio.
```

---

## Element #2 — The Reporter

- **Status:** LOCKED → `elements/02_reporter.png`
- **Omni Reference:** none
- **Used in shots:** 15, 16, 24
- **Scope:** Series-wide lock. Same reporter in every episode's topology-explanation beat.

```
Photorealistic male American news field reporter, mid-40s, seasoned and grounded look, the face of a veteran war correspondent who has been doing this for twenty years. Athletic build, slightly weathered face, short professional haircut, clean-shaven or neatly trimmed short beard. Chest-up framing as if shot by a news camera crew on location. His expression is serious and focused — the look of a reporter who has just been briefed by law enforcement on the ground and is about to tell the anchor what he learned, not smiling, not theatrical, not afraid, just professional and grave.

He holds a plain black stick microphone in his right hand, raised to chest height in the neutral ready-to-speak position. The microphone has absolutely no network logo, no flag, no branded microphone flag, no call letters, no text of any kind. Just a plain black stick mic.

Wardrobe: a charcoal or dark olive-green lightweight field jacket or trench coat over a plain dark shirt, no tie, no visible press credentials, no press pass on a lanyard, no sponsor logos, no flags. The wardrobe is practical and functional for a field correspondent at a cordoned-off scene at night.

The background behind him is slightly out of focus but suggests a night exterior at a crime scene or secured government facility — soft red and blue police light flashes visible as blurred dots of color in the far distance, a sense of cold night air, no specific location readable. No text, no signs, no buildings clearly identifiable — just the vague ambience of "at a cordoned-off scene, at night, emergency lights flashing behind him." Shallow depth of field, his face is sharp and the background is painterly soft.

Cool cinematic news-broadcast lighting on his face — a single bright LED panel held by the off-camera camera crew, giving him a clean well-lit face against the dim night behind him. Slight cinematic vignette around the edges of the frame.

Photorealistic, real broadcast camera, real skin texture, real fabric, real night lighting — the look of a real live network news remote broadcast. Not stylized. Not cartoon. Not Pixar. Not anime. Not a movie-style reporter caricature. Just a real veteran field correspondent at a real scene.

1:1 square aspect ratio.
```

---

## Element #9 — The Exterior Bunker Entrance

- **Status:** LOCKED → `elements/09_bunker_exterior.png`
- **Omni Reference:** none
- **Used in shots:** 5 (dawn wide shot), 15, 16, 24 (night, FBI vehicles, sealed off)
- **Scope:** Part 1 only

```
Photorealistic exterior of a hardened American military bunker entrance cut directly into the base of a rocky mountain, the kind of real underground facility that exists at Cheyenne Mountain Complex or Raven Rock. Massive blast-proof steel doors set into the raw mountain rock, painted dark military green or dull grey, heavy industrial hinges visible, clearly designed to withstand a nuclear strike. The doors are currently closed. The rock face around the entrance is natural unpainted granite or sandstone, rough and textured, with crude rock-cut tunneling visible where the bunker was bored into the mountain.

Two small fortified guard posts flank the entrance, made of reinforced concrete with narrow slit windows. A single heavy steel barrier arm blocks the short access road leading up to the doors. Faded yellow "RESTRICTED AREA — U.S. GOVERNMENT FACILITY" warning signs are visible on the guard posts. A security fence with barbed wire runs across the approach. Razor wire coiled along the top. Cold and utilitarian, no decoration.

The mountain rises dramatically behind and above the bunker entrance, dark jagged rock formations against the sky. The bunker itself is small compared to the mountain — a dark rectangular entrance that looks barely significant against the scale of stone above it, yet clearly impenetrable. The whole scene is grounded in the Colorado or Pennsylvania mountains, pine trees visible at the edges of the frame on the lower slopes.

Lighting: dawn light, low golden sun on the upper mountain rock, cold blue shadow on the bunker entrance itself, sober atmospheric mood. Photographed as a wide establishing shot with the bunker entrance filling the lower-center of the frame and the mountain rising above it.

Photorealistic, real camera, real rock texture, real steel and concrete, real atmospheric perspective, real dawn lighting. The look of a real declassified government photograph of an actual military bunker entrance. Not stylized. Not cartoon. Not Pixar. Not anime. Not a video-game render. Not a sci-fi vault. Just a real hardened American military installation photographed at dawn.

1:1 square aspect ratio.
```

---

## Element #10 — The Interior Bunker Hallway

- **Status:** LOCKED → `elements/10_bunker_interior.png`
- **Omni Reference:** none
- **Used in shots:** 6, 8, 10, 11, 27, 28 (the most reused environment in Part 1)
- **Scope:** Part 1 only

```
Photorealistic interior corridor of a hardened American military underground bunker, the kind of real operational hallway inside Cheyenne Mountain Complex or an old NORAD facility. Narrow reinforced corridor with bare reinforced concrete walls and exposed industrial steel beams along the ceiling. Thick metal cable trays, electrical conduits, ventilation pipes, and water pipes run along the upper wall where it meets the ceiling. The floor is polished concrete or industrial linoleum, scuffed from decades of use.

Heavy steel blast doors set into the corridor walls at regular intervals — each door is riveted industrial metal painted dark military green, with large wheel-latch handles and warning placards. A few of the doors have faded yellow stenciled text and number codes next to them identifying room numbers. The overall feel is 1960s Cold War military engineering still in active use — not modernized, not decorated, grimly functional.

Lighting is dim emergency mode — the main overhead fluorescent fixtures are dark, and the corridor is lit only by red emergency LED strip lights mounted along the upper walls, bathing the whole space in a deep red glow with pockets of near-black shadow. The red emergency lighting is the dominant color of the scene, cold and alarming.

Wide shot looking down the corridor toward a vanishing point in the distance, so the viewer feels the depth of the passage. Empty of people, empty of drones — just the environment itself as a reference image that can be used as a background in later shots. Slight haze or dust particles in the air catching the red emergency light.

Photorealistic, real camera, real concrete texture, real metal, real fluorescent and LED light sources, real atmospheric depth. The look of a real declassified photograph of the interior of an active American military bunker. Not stylized. Not cartoon. Not Pixar. Not anime. Not a video-game corridor. Not a horror-game basement. Just a real underground military facility interior.

1:1 square aspect ratio.
```

---

## Element #16 — The Ballistic Missile

- **Status:** LOCKED → `elements/16_ballistic_missile.png`
- **Omni Reference:** none
- **Used in shots:** 2, 3, 4 (Continuity Sequence A — one continuous missile flight across the Pacific)
- **Scope:** Part 1 only

```
Photorealistic Chinese intercontinental ballistic missile in mid-flight, three-stage solid-fuel design similar to the real Chinese DF-41 or DF-31, long slender cylindrical body painted matte military olive green or dull grey with small faded warning stencils on the side. Pointed nose cone at the top that is clearly a separable payload section — the seam line where the nose cone detaches is visible on the body. Small stabilizer fins near the base of the missile body. Subtle white Chinese military stenciled markings along the fuselage, not readable as specific characters but suggesting real military identification markings. No Chinese flag, no red stars, no cartoon decoration, no fictional branding.

The missile is shown in flight at high altitude above clouds, slightly angled as if in the middle of its trajectory. The engine at the base is firing, a bright white-orange plume of rocket exhaust trailing behind it, illuminating the surrounding air with a soft glow. Thin wispy high-altitude clouds and stars visible in the background — we are clearly above the troposphere, in the upper atmosphere.

Wide atmospheric shot, the missile takes up roughly the central third of the frame vertically, with sky and clouds around it. Photorealistic, real camera, real metal body texture, real rocket exhaust plume, real atmospheric perspective. The look of a real declassified photograph of an active ballistic missile in flight, the kind of still image that would appear in a defense intelligence report. Not stylized. Not cartoon. Not Pixar. Not anime. Not a video-game render. Not a sci-fi spaceship. Just a real Chinese ballistic missile in mid-flight.

1:1 square aspect ratio.
```

---

## Element #19 — The FBI Clipboard + Paper + Pen

- **Status:** LOCKED → `elements/19_fbi_clipboard.png`
- **Omni Reference:** none
- **Used in shots:** 17 (star drawing), 21 (tree drawing)
- **Scope:** Part 1 only
- **Notes:** Element #5 (FBI agent's hand) reuses this as Omni Reference. Both shots 17 and 21 show the same clipboard, so continuity matters.

```
Photorealistic overhead close-up of a standard American law enforcement metal clipboard — the classic dark aluminum or steel clipboard used by FBI agents, police officers, and military personnel, with a spring-loaded clip at the top. The clipboard is about 9 by 12 inches, lying flat on a dark neutral surface. A fresh blank sheet of off-white legal-pad paper is secured under the clip — the paper is slightly yellowed, has horizontal ruled lines in pale blue, and shows a faint vertical red margin line on the left. The paper is completely blank — no text, no drawings, no marks, no handwriting, nothing on it yet. Just a fresh blank page ready to be written on.

Next to the clipboard, a plain black ballpoint pen rests on the same dark surface — a standard utilitarian office pen, uncapped, black plastic body, no branding, no logo, ready to be picked up. The pen is positioned diagonally across the corner of the clipboard as if just set down a moment ago.

Lighting is even and slightly cool, from above and slightly to the side, casting a soft shadow from the clipboard onto the dark surface below. The surface underneath is a dark grey or near-black desk or table, slightly textured, out of focus at the edges. No other objects in the frame — no phone, no coffee cup, no badge, no folder. Just the clipboard with blank paper and the pen.

Overhead top-down camera angle, square aspect ratio, the clipboard fills most of the frame. Photorealistic, real metal clipboard texture, real paper fiber, real pen plastic, real shadows. The look of a real evidence photograph or law enforcement documentation still. Not stylized. Not cartoon. Not Pixar. Not anime. Not a stock-photo mockup. Just a real FBI clipboard and pen photographed from above.

1:1 square aspect ratio.
```

---

## Element #5 — The FBI Agent's Gloved Hand

- **Status:** LOCKED → `elements/05_fbi_hand.png`
- **Omni Reference:** **`elements/19_fbi_clipboard.png`** (for clipboard and pen continuity)
- **Used in shots:** 17, 21
- **Scope:** Part 1 only

```
Photorealistic overhead close-up of an FBI agent's gloved right hand holding a plain black ballpoint pen, poised over a fresh blank sheet of off-white legal-pad paper on a dark metal clipboard. The hand is wearing a black tactical nitrile glove, close-fitting, the kind used by federal law enforcement at crime scenes — thin black rubber, matte finish, not shiny, gripping the pen naturally in a writing position between the thumb and first two fingers.

The rest of the agent's arm is visible up to about the wrist or lower forearm, where the dark sleeve of a plain navy-blue or black tactical jacket is visible. No wristwatch, no jewelry, no rings, no name tag visible in frame. Just the gloved hand and a bit of dark sleeve.

The pen tip is hovering just above the paper, about to draw a shape — the hand is mid-motion, not yet touching the paper, capturing the exact moment before a stroke is made. The paper is still completely blank. No drawings yet, no writing, no marks.

Lighting is even and slightly cool from above, the same lighting as a crime-scene documentation photograph. Soft shadow cast by the hand and the clipboard. The dark neutral surface under the clipboard is out of focus at the edges. No other objects in frame — no other hand, no face, no badge, no phone, just the gloved hand on the clipboard.

Overhead top-down camera angle. Photorealistic, real nitrile glove texture, real pen plastic, real paper fiber, real fabric on the sleeve. The look of an evidence documentation photograph. Not stylized. Not cartoon. Not Pixar. Not anime.

1:1 square aspect ratio.
```

---

## Element #6 — The American Generals

- **Status:** LOCKED → `elements/06_american_generals.png`
- **Omni Reference:** **`elements/10_bunker_interior.png`** (for the bunker atmosphere — red emergency lighting, concrete walls)
- **Used in shots:** 12
- **Scope:** Part 1 only
- **Notes:** Element #12 (bunker sub-level conference room) is MERGED into this element. The generals were generated inside their conference room in one pass, so we do not need a separate room element.

```
Photorealistic small military conference room inside an underground American bunker. Three senior American military generals, men in their 50s and 60s, seated around a dark wooden conference table in full US military dress uniform — crisp dark green or navy uniform jackets with rows of colorful service ribbons and campaign medals on the chest, silver stars on the shoulders indicating general rank, neat graying hair, clean-shaven faces. They are frozen in place, staring in wide-eyed horror at something happening just off-camera to their left, mouths slightly open, bodies tensed, one general gripping the edge of the table, another half-rising from his chair. Real fear and disbelief on their faces — the expression of men who have just realized something they were told was impossible is actually happening to them right now.

The conference room is small and utilitarian — bare reinforced concrete walls like the rest of the bunker, exposed cable conduits along the upper walls, a single dim overhead light fixture, a red emergency LED strip along one wall bathing the whole room in a cold red glow. A few open manila folders and coffee cups are scattered on the conference table where the meeting was in progress. A framed American flag is mounted on the wall behind them.

Wide shot at slightly low angle, framed so all three generals are visible around the table with their reactions clearly readable. The drones that they are reacting to are NOT in the frame — only their faces tell us what is happening. Cold red emergency lighting dominates the scene with pockets of near-black shadow at the edges.

Photorealistic, real faces, real uniform fabric, real military insignia, real bunker interior, real red emergency lighting. The look of a still frame from a serious military drama. Not stylized. Not cartoon. Not Pixar. Not anime. Not theatrical. Just three real American generals at the exact moment they realize they are in a situation their training never prepared them for.

1:1 square aspect ratio.
```

---

## Still to generate (six elements remaining)

| # | Element | Used in shots | Notes |
|---|---|---|---|
| 11 | Industrial ventilation shaft | 7 | Drones entering through the vent |
| 13 | California data center | 18 (intact), 20 (burning) | Two variants — intact and burning |
| 14 | Pentagon war room | 26 | Dark monitors, stunned officers |
| 20 | Raspberry Pi + small drone | 31 | Scale shot, hand holding the Pi |
| 21 | Phone showing GitHub page | 32, 33 | Phone screen showing MadHoney repo |
| 22 | Classified document with WRONG TOPOLOGY stamp | 30 | The "wrong topology" land beat |

Prompts for these six will be added to this file as they are generated in later sessions.

---

## Rules for future sessions working on this file

## Element #14 — Pentagon War Room

- **Status:** LOCKED → `elements/14_pentagon_war_room.png` (locked on first generation, 1 iteration)
- **Omni Reference:** none
- **Used in shots:** 26
- **Scope:** Part 1 only, one-shot usage
- **Notes:** Real Pentagon command and control room aesthetic — not Hollywood war room, not sci-fi. Massive video wall dominating the back of the room, tiered operator workstations, uniformed officers seen from behind. Should feel like a real declassified photograph of a command center during a major incident, not an action movie set.

```
Photorealistic wide interior shot of a real American Pentagon-style military command and control room during an active crisis, seen from the back of the room looking forward toward a massive wall of monitors. The room is a large rectangular tiered operations center, the kind of hardened underground command facility the US military actually uses — not a Hollywood movie set, not a sci-fi war room, a real functional space.

The far wall, directly across from the camera, is dominated by an enormous video wall: a grid of dozens of large flat-panel monitors tiled seamlessly together, twenty to thirty feet wide and two stories tall. The screens display a mix of real-looking operational content: a large geopolitical map of the continental United States with red warning markers scattered across it, several feeds showing satellite or drone imagery of industrial-looking targets, a couple of screens showing scrolling data dashboards and status readouts, one screen showing a live news broadcast with a "BREAKING" chyron at the bottom. The monitor wall is the brightest thing in the room and it casts a cool blue-white glow across the entire space.

In front of the monitor wall, arranged in tiered rows like an amphitheater descending toward the screens, are rows of dark grey operator workstations — modular desks with multiple smaller monitors, keyboards, headsets, phone handsets, and low task lamps. Each workstation has a uniformed American military officer seated at it, wearing current-era US military service dress in muted tones — Army, Navy, Air Force, Space Force — visible from behind and in three-quarter profile, leaning forward intently, clearly working a live crisis. Some officers are standing, some are talking on phones, some are gesturing at their screens. The atmosphere is tense but disciplined, not panicked, not chaotic.

The ceiling is high and functional, with recessed architectural lighting and exposed cable trays running overhead. The side walls are dark grey acoustic panels with a few smaller secondary displays showing regional maps and clocks labeled with timezones (Washington DC, London, Tokyo, Moscow). The floor is dark industrial carpet. American flags stand on low flag stands in the corners of the room, partially visible at the edges of the frame.

Lighting is the cold blue-white wash from the giant monitor wall dominating the back of the room, mixed with warmer task-light pools at each workstation and soft cool ambient ceiling light. The color palette is blue-grey and slate, with accents of warm amber from the task lamps and hot red from the warning markers on the main map. The overall feel is exactly what you would expect from a real declassified photograph of a Pentagon command center during a major national incident.

The camera is positioned at the back of the room, slightly elevated, looking forward and slightly down, so the tiered workstations descend into the frame and the camera has a clear view of the big monitor wall beyond them. Wide cinematic framing, deep focus, the full length of the room visible from the near operator seats all the way to the video wall.

No faces visible in focus — officers are seen from behind or at three-quarter profile, their identities not the subject, the room itself is the subject. No brand logos on the monitors, no real news network names, no fictional flags, just generic American military context. Photorealistic, real monitor glow, real uniform fabric, real task-light pools, real architectural depth. Not stylized. Not cartoon. Not Pixar. Not anime. Not a video game cutscene. The look of a real still frame from inside a real Pentagon command and control room during a real crisis.

1:1 square aspect ratio.
```

---

## Element #13 — California Data Center (intact state)

- **Status:** LOCKED → `elements/13_data_center.png` (locked on first generation, 1 iteration; burning variant for Shot 20 still pending, will reuse this as Omni Reference)
- **Omni Reference:** none (this element will BE the Omni Reference for the burning-state variant used in Shot 20)
- **Used in shots:** 18 (intact), 20 (burning — generated later as a variant using this locked image as Omni Reference)
- **Scope:** Part 1 — may reappear in later episodes
- **Notes:** Single hyperscale-data-center element that needs to work in two states. This prompt locks the intact "before" state for Shot 18. The burning version for Shot 20 will be a separate OpenArt pass using this locked PNG as Omni Reference with an edit prompt adding fire/smoke damage. Must read as a real anonymous Central Valley data center — windowless, beige-grey concrete, hundreds of HVAC units lined up on the roof (this is the defining visual signature), chain-link fence with barbed wire, backup generators, dry California hills in the background. No branding, no logos, no company name. No people, no vehicles.

```
Photorealistic wide exterior shot of a real American hyperscale data center building in rural Northern California, photographed in the soft golden light of early morning, roughly 45 minutes after sunrise. The building is a long, low, flat-roofed industrial structure, hundreds of feet long, finished in plain beige-grey concrete panels and corrugated metal, completely windowless along its visible length. The look is utilitarian and anonymous, like a giant warehouse with no branding, no logos, no signs, no company name anywhere on it. This is the kind of facility big tech companies build out in the California valleys specifically so nobody pays attention to them.

Running along the entire length of the roof are rows and rows of large commercial HVAC units — industrial rooftop cooling equipment, rectangular metal boxes in dull grey and off-white, lined up in neat parallel ranks. The HVAC units are the defining visual feature of the building: dozens of them, identical, clearly visible from the camera's slightly elevated three-quarter angle, a mechanical landscape on top of the roof. Thick insulated pipes and bundled cable trays run between some of the units. A few thin chimneys or exhaust stacks rise above the roofline.

The building sits in a wide empty concrete and gravel lot, surrounded by a low chain-link perimeter fence topped with three strands of barbed wire. Inside the fence line are a couple of large outdoor electrical transformers, a row of backup diesel generators in weatherproof enclosures, and industrial-grade cable runs going into the building wall. Outside the fence, beyond the lot, the California landscape: dry golden-brown grass, a few scattered oak trees, low rolling hills in the distance fading into soft atmospheric haze. The sky is a pale clean blue with maybe one or two thin wisps of morning cloud.

The camera position is a slightly elevated three-quarter angle, roughly 20 degrees above horizontal, showing both the front facade and one long side of the building, and giving a clear view of the HVAC-covered roof. The building fills most of the frame horizontally, with a generous amount of dry California hillside visible behind it and a strip of lot and fence in the foreground.

The lighting is early-morning golden hour, soft and warm, coming from roughly behind the camera's left shoulder, casting long gentle shadows from the HVAC units across the roof and from the building itself across the lot. The whole scene feels quiet, empty, anonymous, nothing is happening yet. No people in the frame, no vehicles in the lot, no activity on the roof, no smoke, no fire, no damage. This is the "before" state — intact, clean, functional, unremarkable, the way it looked for every single day of its operational life right up until the moment the drones arrived.

Photorealistic, real concrete panel texture, real HVAC unit detail, real California morning light, real atmospheric perspective. Wide cinematic framing. Not stylized. Not cartoon. Not Pixar. Not anime. Not a 3D render. Not a video game environment. The look of a real satellite-imagery or drone-photography shot of an actual operating hyperscale data center in the Central Valley.

1:1 square aspect ratio.
```

---

## Element #11 — Industrial Ventilation Shaft

- **Status:** LOCKED → `elements/11_ventilation_shaft.png` (locked on first generation, 1 iteration)
- **Omni Reference:** none
- **Used in shots:** 7 (drones entering the bunker through the vent)
- **Scope:** Part 1 only, one-shot usage
- **Notes:** This is the moment just before the drones breach. Empty shaft, no drones visible yet. Must feel like it connects to Element #10 (interior bunker hallway) — same cold industrial palette, same emergency-red bleed at the distant end. Long tunnel perspective, strong depth, vanishing point centered.

```
Photorealistic wide shot of the interior of a large industrial ventilation shaft inside an American hardened military bunker, seen from inside the shaft looking along its length. The shaft is a rectangular metal duct, roughly two meters wide and two meters tall, made of thick riveted galvanized steel panels with faint seams and bolt lines where the panels join. The inside walls are dull matte grey with a faint bluish tint from old paint, scuffed and lightly scratched in places from decades of maintenance, with thin streaks of rust near the seams. The metal surfaces catch light in a dull, matte, industrial way, not shiny, not polished.

Running along the top of the shaft at regular intervals are small recessed service lights behind metal grilles, emitting a cold blue-white glow that creates long thin parallel highlights down the length of the duct and deep shadows in the corners. The lighting feels cold, emergency, functional, the kind of light a maintenance crew would install for once-a-decade access, not for people to be comfortable in.

The camera is positioned inside the shaft, roughly centered, looking straight down its length. The shaft stretches off into the distance, fading into darker shadow, giving a strong sense of depth and tunnel-like perspective. The vanishing point is in the center of the frame. The floor of the shaft is the same riveted metal as the walls, slightly dusty, with faint scuff marks from equipment that has been dragged through over the years.

At the far end of the shaft, partially silhouetted against the faint light from the next section, the camera sees the dim outline of a heavy metal ventilation grate — a vertical array of thick horizontal metal bars or louvered slats set into a steel frame, the kind of grate that separates shaft segments in a secure facility. Behind or around the grate, very faint red emergency lighting bleeds in from the room on the other side, giving the grate and the surrounding darkness a subtle red edge.

Small details reinforce the military-industrial feel: a stenciled yellow-and-black warning label on one wall panel with unreadable small text, an inspection sticker near a seam, a thin cable run pinned along the upper corner of one wall. Nothing in the shaft is cartoon or stylized, everything is utilitarian, built for function, built for decades of quiet service.

No people, no drones, no insects, no visible machinery in the frame. Just the empty shaft, the cold overhead lights, the distant grate, and the bleed of red emergency light around it. This is the moment just before something enters, not the moment of entry.

Photorealistic wide shot, cinematic framing, deep focus, the full length of the shaft visible from near-camera to the distant grate. Real metal texture, real dust, real industrial lighting, real long-exposure depth. Not stylized. Not cartoon. Not Pixar. Not anime. Not a video game render. The look of a still frame from a grounded cinematic thriller set inside a real American military bunker.

1:1 square aspect ratio.
```

---

## Element #22 — Classified Document with WRONG TOPOLOGY stamp

- **Status:** LOCKED → `elements/22_classified_document.png`
- **Omni Reference:** none
- **Used in shots:** 30 (the canonical buzzword punchline — TOPOLOGY)
- **Scope:** Part 1 only, one-shot usage
- **Notes:** This is the visual punchline of the series' canonical buzzword. The star topology diagram must be instantly recognizable (one central hub, multiple spokes) because that IS the thing Nir is calling wrong. The red "WRONG TOPOLOGY" stamp must be legible — that is the whole joke. Locked on first generation, 1 iteration.

```
Photorealistic overhead top-down close-up of a single page of a real American government classified document, lying flat on a dark neutral desk surface. The paper is standard US Letter size, slightly off-white, very faintly yellowed, with the subtle fiber texture of real printer paper, crisp edges, minimal wrinkle.

The page has a thick solid red banner stripe running across the very top of the paper and another identical red banner stripe running across the very bottom, in the unmistakable style of a real declassified US government classified document. In bold white sans-serif capital letters centered inside both the top and bottom red banners, the word "CLASSIFIED" is printed. These banners are the standard US government classification marking format — not stylized, not cartoon, not fictional — the exact format a real leaked Pentagon document would show.

Below the top red banner, a bold black sans-serif title is printed in large capital letters across the width of the page: "U.S. MILITARY AI ARCHITECTURE". Directly beneath the title, a smaller subtitle line reads "CLASSIFIED — INTERNAL USE ONLY". No real agency name, no real seal, no real insignia — just the generic classified-document look.

Below the title, occupying most of the page, is a clean technical architecture diagram drawn in thin black lines on the white paper. The diagram is unmistakably a STAR TOPOLOGY: one single large labeled node in the exact center of the diagram, labeled "CENTRAL MODEL", drawn as a circle or rounded rectangle. Radiating out from this central node are six to eight straight thin black lines, each ending in a smaller labeled peripheral node drawn as a smaller circle or rounded rectangle, positioned in a rough circle around the center. The peripheral nodes have short generic technical labels like "SENSOR 1", "SENSOR 2", "FIELD UNIT", "COMMAND", "LOGISTICS", "INTEL", "ANALYSIS", "TARGETING". Every single line connects ONLY to the center — no peripheral node is connected to any other peripheral node. This is a pure textbook star topology and it must read as one at a glance.

Slammed diagonally across the diagram, rotated roughly 15 to 20 degrees counter-clockwise, is a huge red rubber-stamp imprint of the words "WRONG TOPOLOGY" in bold blocky capital sans-serif letters. The stamp is saturated red ink, with authentic uneven ink coverage — slightly heavier on one side, slightly broken and patchy on the other, small spots where the ink did not fully transfer, faint red bleed at the edges of each letter. The stamp is large — it spans roughly two-thirds the width of the diagram — and it clearly overlaps and partially obscures the center node and several of the spokes, as if someone slammed it down furious and off-center. The "WRONG TOPOLOGY" stamp text is completely legible despite the ink irregularities.

Lighting is even, slightly cool, from above and slightly to the side, the way a real evidence photograph or an FBI case-file scan would be lit. A soft shadow is cast by the paper onto the dark desk below. The dark desk surface is just barely visible at the edges of the frame, slightly out of focus. No other objects in the frame — no coffee cup, no pen, no folder, no hand, no phone, no badge. Just the one classified document page, flat, overhead, isolated.

Overhead top-down camera angle, square aspect ratio, the document fills almost the entire frame with a small amount of dark desk visible around it. Photorealistic, real printer paper fiber, real printer toner, real red rubber stamp ink texture, real paper shadow. The look of a real leaked classified document photograph of the kind that would appear on the front page of a newspaper. Not stylized. Not cartoon. Not Pixar. Not anime. Not a vector graphic. Not a PowerPoint slide. Not a UI mockup. A real photographed printed page.

1:1 square aspect ratio.
```

---

1. **Every new element prompt gets added to this file as it is generated, in the same format as the ones above** — element number, status, Omni Reference, shots, scope, any iteration notes, and the full prompt in a code block.
2. **Never delete iteration history.** If an element is regenerated later, keep the old prompt labeled SUPERSEDED and add the new one — future sessions need to know what did NOT work.
3. **Cross-reference `PART_1_ELEMENTS.md` status tracker** — when you add a prompt here, also update the status in that file. The two files stay in sync.
4. **If the rules in `VISUAL_HOOK_RULES.md` Rule 4 or `FIGHT_METAPHOR_RULES.md` change**, all existing prompts may need to be audited for compatibility. Flag any conflicts before generating new elements.
