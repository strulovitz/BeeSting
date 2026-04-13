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

**It carries backups.** Pre-positioned, pre-flying, pre-identical-looking backups. The architecture is redundant by design — every DwarfQueen has one or more backup DwarfQueens in the same swarm, already flying, already running the same big model on the same heavy hardware, already in contact with the rest of the swarm. If the primary DwarfQueen is destroyed, a backup DwarfQueen takes over her squad in the same second — not because anything got promoted, but because the backup was already a DwarfQueen, flying beside her, doing nothing in particular until she was needed.

The same goes one level up — every GiantQueen has backup GiantQueens. And one more level up — the RajaBee has backup RajaBees. **Redundancy is built into the swarm from the moment of launch.**

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

## One-line summary for every script

> **The swarm has many small brains and many backup queens. The brains are all different sizes, so Workers cannot become Queens — only backup Queens can. All the drones look the same from outside, so nobody can tell the leader from a foot soldier. The drones whisper to each other in a few words at a time, so there is no signal to jam and no base to bomb. Every drone is thinking for itself, and the whole swarm changes its plan whenever it hits a wall. The software is free on the internet tonight.**

Keep this one-line summary at the top of your head while drafting any BeeSting script. Every sentence you write should be consistent with it.
