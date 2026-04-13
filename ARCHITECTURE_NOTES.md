# KillerBee Architecture Notes for Video Scripts

**Decision date: 2026-04-13**

Short, locked reminders about the underlying KillerBee architecture that every script must respect. These are not creative choices — they are technical facts about how the system actually works. Getting them wrong in a script makes the whole video feel fake to anyone who understands the system, and invites pedantic nitpicking that kills forwarding velocity.

If you are drafting a script for any episode of BeeSting and you find yourself writing a sentence that contradicts one of the rules below, stop and rewrite. The rules are ranked by how often Claude has gotten them wrong historically. Number 1 is the one to double-check every single time.

---

## Rule 1 — Workers CANNOT become Queens. Ever.

**This is the rule Claude keeps getting wrong.** Read it, then read it again.

In KillerBee, the Workers, the DwarfQueens, the GiantQueens, and the RajaBee run different hardware and different model sizes. A Worker runs a small cheap model (a few billion parameters) on a tiny chip like a Raspberry Pi. A DwarfQueen runs a larger model on much beefier hardware — extra compute, extra memory, extra power. A GiantQueen runs a still larger model on even beefier hardware. The RajaBee runs the biggest model on the heaviest hardware.

**A Worker cannot be promoted to DwarfQueen when the DwarfQueen dies.** The Worker's hardware physically cannot run the DwarfQueen's model — not enough memory, not enough compute, not enough anything. A Worker that tried to take over a DwarfQueen's job would either crash or would run the DwarfQueen's model so slowly that the whole swarm would collapse waiting for it.

**The same applies at every level of the hierarchy.** DwarfQueens cannot be promoted to GiantQueens. GiantQueens cannot be promoted to RajaBees. Each level up requires hardware the level below does not carry.

### How the swarm actually handles the death of a leader

**It carries backups.** Pre-positioned, pre-flying, pre-identical-looking backups. The architecture is redundant by design — every DwarfQueen has one or more backup DwarfQueens in the same swarm, already flying, already running the same big model on the same heavy hardware, already in contact with the rest of the swarm. If the primary DwarfQueen is destroyed, a backup DwarfQueen takes over her squad in the same second — not because anything got promoted, but because the backup was already a DwarfQueen, doing nothing in particular until she was needed.

The same goes one level up — every GiantQueen has backup GiantQueens. And one more level up — the RajaBee has backup RajaBees. **Redundancy is built into the swarm from the moment of launch.**

### Backups are SPREAD ACROSS the swarm — never clustered

**Critical detail Claude has gotten wrong.** Backup Queens do not fly close to the primary Queen. Backup RajaBees do not fly close to the primary RajaBee. They are deliberately **scattered across the entire swarm formation**, hidden among the Workers, far from the leader they would replace.

The reason is brutally obvious once you say it: if the enemy throws one grenade, fires one mortar shell, drops one bomb, or gets one lucky burst of gunfire, you do not want it taking out the primary Queen and all of her backups in the same explosion. So the swarm spaces them out. Different rooms. Different altitudes. Different parts of the formation. A primary Queen leading the breach in one corridor; her backup Queen flying with a different group of Workers two corridors away, doing what looks like ordinary Worker work, until the moment the primary dies and the backup takes over the role. Same for RajaBees.

**In scripts, when the redundancy beat appears, always say "spread" or "scattered" or "hidden among the workers" — never "flying right behind her" or "flying alongside her" or "flying close to the primary."** The whole point is that they are not close.

Language to use:
- *"Another queen was already flying somewhere else in the swarm, scattered far from the one we just killed, hidden among the small drones."*
- *"The swarm carries its backup queens spread across the whole formation, so that no single grenade and no single bullet ever takes them out together."*
- *"You cannot kill the leadership, because the leadership is everywhere at once and nowhere in particular."*

Language to **never** use:
- ~~"Another queen was flying right behind her."~~ (Wrong. They are scattered, not in formation behind the primary.)
- ~~"The backup queens stayed close to the primary so they could take over quickly."~~ (Wrong. Closeness is the failure mode the scattering is designed to prevent.)
- ~~"The backup queens were flying in tight formation."~~ (Wrong. The opposite of tight.)

### Why all the drones look identical from outside

Because the external shape, size, weight, and flight signature are deliberately made identical across Workers, DwarfQueens, GiantQueens, and RajaBees. The Worker's internal compartment holds ammunition. The DwarfQueen's holds a bigger computer. The GiantQueen's holds an even bigger computer. The RajaBee's holds the biggest. But the housings are balanced to weigh the same and look the same. An enemy sniper, an interceptor drone, a soldier in a hallway — none of them can tell which drone is a queen and which is a worker. They all look alike. They all fly alike. And there are multiple queens and multiple backups of every kind, hidden among the workers.

**This is the whole reason the swarm is so hard to decapitate.** You cannot kill the leader, because you cannot find the leader. You cannot kill "the leadership," because the leadership is redundant. And you cannot wait for the swarm to promote a Worker into a gap in the leadership, because Workers physically cannot take the job.

### Language to use in scripts

When the manager paragraph or the anchor's delivery reaches for a redundancy beat, use language like:

- *"They destroyed one queen. Another queen was already flying in the swarm, carrying the same heavy brain, doing the same job. Behind her, another."*
- *"The swarm was built with backup queens from the start — because workers are too small and too slow to ever take a queen's job, so the swarm brings extra queens along with it."*
- *"Every drone looked identical from outside. The queens and the workers are the same shape and the same weight. The only difference is what is packed inside, and you cannot see inside from across a hallway."*

Language to **never** use:

- ~~"The swarm promoted a worker to replace the dead queen."~~ (Wrong. Workers cannot do this.)
- ~~"Another worker took over the queen's job."~~ (Wrong. Workers cannot do this.)
- ~~"The swarm elected a new leader from among the drones that were left."~~ (Wrong. The new leader was already flying as a backup — she was not elected from survivors, she was pre-positioned.)

---

## Rule 2 — The drones talk to each other, not to a base.

The KillerBee communication model is short encrypted text passed directly between drones. Not video. Not model weights. Not streamed sensor data. Just a few words at a time, like bees waggle-dancing in a hive.

This is the architectural reason the swarm can operate:
- Inside a Faraday cage (like a bunker), because there is no outside signal to depend on.
- Under heavy jamming, because even the worst military radio has enough bandwidth for short text.
- Underwater, over acoustic links that cannot carry anything richer than a few hundred bits per second.
- At intercontinental distance with no cloud connection.

**In scripts, the phrase is: "the drones talk to each other, not to a base."** Or: *"they whisper to each other in a few words at a time."* Or: *"the swarm is coordinated by short messages passed from drone to drone, like bees in a hive."* All three are acceptable.

Language to **never** use in a script:
- ~~"The drones are controlled from a central server."~~ (Wrong. That is the old way, the American way, the thing our system is defined against.)
- ~~"The swarm shares its AI model across the drones."~~ (Wrong. Each drone has its own complete model. No sharing.)
- ~~"The swarm needs an internet connection to coordinate."~~ (Wrong. Local encrypted radio only.)

---

## Rule 3 — Each drone has its own complete brain. The brains are small.

Every Worker drone carries its own complete AI model. Every DwarfQueen drone carries her own complete (larger) model. Every GiantQueen carries her own complete (still larger) model. The RajaBee carries her own complete (biggest) model.

**No model is split across drones.** Nobody is running half a brain on one drone and half on another. This is the thing that approaches like Petals and Exo try to do, and it does not work over battlefield radio because the bandwidth is too low.

The Worker's brain is small enough to run on a chip the size of a credit card, costing about what a dinner costs. The DwarfQueen's brain is bigger and needs a bigger chip. The GiantQueen's is bigger still. The RajaBee's is the biggest.

**In scripts, this is the line: "Every drone has its own brain."** Or: *"Each drone is thinking for itself."* Or: *"Small cheap drones, each with its own small cheap brain, combining into one big brain by talking to each other."*

---

## Rule 4 — The brain is free, the body is cheap, the software is open source

The KillerBee software is free on GitHub. Anyone can download it. The AI models the Workers run (DeepSeek, Qwen, small quantized open-weight models) are also free to download. The hardware is consumer-grade — the drone bodies are standard Chinese FPV drones and the chips are standard consumer AI chips.

The entire system is legal to possess in every country on Earth, because there is nothing weapon-like about any one piece of it individually. The weapon is in the coordination, and the coordination is in a few lines of open-source code that nobody can embargo.

**In scripts, the emphasized phrase is always: "Free. On the internet. Tonight."** Or: *"Anyone with a laptop can download it."* Or: *"The Chinese military downloaded it off the internet last month. For free."*

---

## Rule 5 — The swarm adapts in real time

Because every drone is thinking for itself and every drone is in short-text contact with the others, the swarm can:

- **Breach and enter** — one drone sacrifices itself to blow open a door or a window, the rest follow through.
- **Reroute around obstacles** — if a hallway is blocked, the swarm finds another way, usually by exploding through a ceiling, a wall, or an air vent.
- **Recognize decoys** — if one drone sees something that looks like a radar or a generator but does not behave like one, it reports back and the swarm ignores the decoy.
- **Opportunity recognition** — if one drone sees a high-value target nobody planned for (a fuel truck next to a building, a vehicle convoy), it reports back and the swarm redirects on the spot.
- **Autonomous target identification** — multiple drones can observe the same target from different angles, combine their observations, and collectively make an identification that no single small drone could make alone.

**In scripts, the key phrase is: "The swarm changed its plan whenever it hit a wall."** Or: *"When one drone saw something the others did not, it told them, and the whole swarm reorganized in the same second."* Or: *"The swarm did not stop when it was blocked. It found another way."*

---

## Rule 6 — There is no single thing to kill

Combining Rules 1 through 5: the swarm has no single point of failure. There is no command server to bomb, no leader to shoot, no cloud brain to EMP, no satellite link to jam, no operator to kill. Every drone thinks. Every queen has backups. Every level of the hierarchy is redundant. Every communication is short, local, and distributed. Every model is free and already downloaded.

**In scripts, the line is: "You cannot kill the swarm by killing one drone."** Or: *"There is no base. There is no leader. There is nothing to unplug."* Or: *"Killing one drone changes nothing. Killing one queen changes nothing. There is no heart to hit."*

This is the single most forwardable technical fact about KillerBee, because it is the thing the viewer is instinctively looking for in every news report about a new weapon — *"how do we stop it?"* — and the honest answer is *"you do not."*

---

---

## Rule 7 — TOPOLOGY is the canonical buzzword for the entire BeeSting series

**Decision date: 2026-04-13.** From now on, every BeeSting episode that needs to explain *why* this works uses one single buzzword across the whole series: **topology**.

### Why this word, and why one word

The bible already establishes that the videos must convert a generic AI fear into a swarm AI fear (Conversion 2), and that the technique is to *rename* an existing fear rather than teach a new concept. The word "swarm" was the previous answer, and it still does the job for the angel — every viewer already knows what a swarm of bees or drones feels like.

But the manager — the second audience, the one inside the God paragraph, the one who decides — needs one extra thing the secretary does not need. **He needs a word he can repeat at his own meetings on Monday morning.** A word that sounds smart enough to make him look smart in front of his peers, but simple enough that he can actually explain it without panicking. A word that gives him the feeling of *understanding* the new threat, instead of just being scared of it. A word he will then evangelize for free, because saying it makes him feel like the smartest person in the room.

**That word is "topology."** It is technical enough to feel like insider language. It is short enough to remember. It has a real, true meaning that maps cleanly to the architectural difference between the old American way and the new Chinese way. And the moment the manager can draw a star and a tree on a napkin and explain the difference to a colleague, he becomes our salesperson — for free, in the elevator, at the country club, on the conference call.

### The two shapes the manager must learn

Every BeeSting episode that touches military or technical content uses the same two shapes, with the same names:

**1. The Star (American shape — the one that just lost):**
One big brain in the middle, sitting in a building somewhere on the ground. Many small dumb leaves at the edges, each connected back to the brain in the middle by its own single line. The leaves never talk to each other. They only talk to the brain. Kill the brain in the middle, every leaf dies in the same second. This is how every American drone fleet, every American military AI program, every American cloud AI service, and every American centralized data system has been built for decades. **It is one heart with many limbs.** It is the thing that lost over the Pacific three weeks before Part 1 opens, when one Chinese hypersonic missile hit one California data center and every American drone over the ocean lost its mind in the same instant.

**2. The Tree (Chinese / KillerBee shape — the one that just won):**
Imagine the American military's own command hierarchy. A few generals at the very top, leading the whole operation. Each general has a few colonels under him, leading medium-scale tactical decisions. Each colonel has a few lieutenants under him, leading small-scale decisions. Each lieutenant has a few soldiers under him, doing the actual work — shooting, exploding, photographing, sensing. Now picture every single rank in that hierarchy as a drone: every general, every colonel, every lieutenant, every soldier. There is no human in the chain anywhere. The whole tree is made of small drones with their own brains, talking to each other in a few words at a time, making decisions in lightning speed. **This is many small brains organized into a tree.** It has no single heart to hit, because the leadership is spread across the whole tree, with backup generals and backup colonels scattered hidden among the soldiers.

### How to use the word in scripts

The reporter introduces the buzzword in Act 2 first half, while still in the news-broadcast frame. The reporter is at the scene, stands near the destroyed bunker entrance, has just spoken with FBI counter-terrorism agents on the ground, and brings the explanation to the anchor and the home audience in plain American news voice.

The reporter says **the FBI agents kept using one word — they called this a new topology.** Then he explains that topology just means shape. Then he draws the two shapes (star vs tree) using the American-military-hierarchy analogy, because every American immediately understands generals → colonels → lieutenants → soldiers. Then he lands the punch: the star just lost, the tree just won, and tonight for the first time in history the tree was theirs.

**The word "topology" should appear in every BeeSting episode after Part 1 — at least once per episode**, ideally from the same field-reporter format, so the recurring buzzword becomes a recurring signature of the series. By Part 5 or Part 6, a viewer who has watched the earlier episodes hears the word "topology" and knows what it means before the reporter even explains it. By Part 10, the viewer is repeating it in the elevator. **That is the engine of forwarding velocity.**

Variations on the word are allowed for visual freshness — *"the new topology" / "the tree topology" / "the wrong topology" / "a topology America has never built"* — but the root word stays the same across all 14 episodes.

### Language to use

- *"The FBI agents kept using one word. They called it a new topology."*
- *"Topology just means shape."*
- *"The star just lost. The tree just won."*
- *"America built the wrong topology."*
- *"The Chinese topology has no heart. The American topology has one heart, in one building, in California."*
- *"This is what a tree topology looks like when it is made of small drones."*

### Language to never use

- ~~"This is a new kind of distributed neural network architecture."~~ (Jargon. The word the manager wants is "topology," not "distributed neural network architecture.")
- ~~"This is hierarchical swarm intelligence with multi-agent coordination."~~ (Jargon. Same problem.)
- ~~"The shape of the Chinese system."~~ (Weak. Use the buzzword. The whole point of having a buzzword is that we use it.)

---

## One-line summary for every script

> **The swarm has many small brains and many backup queens, scattered hidden across the whole formation. The brains are all different sizes, so Workers cannot become Queens — only the pre-positioned backup Queens can. All the drones look the same from outside, so nobody can tell the leader from a foot soldier, and one grenade cannot kill the leadership because the leadership is not in one place. The drones whisper to each other in a few words at a time, so there is no signal to jam and no base to bomb. Every drone is thinking for itself, and the whole swarm changes its plan whenever it hits a wall. The shape of the system is a tree, not a star. Topology is the word the manager learns to repeat. The software is free on the internet tonight.**

Keep this one-line summary at the top of your head while drafting any BeeSting script. Every sentence you write should be consistent with it.
