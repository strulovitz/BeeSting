GITHUB URL SHEET — verify in 60 seconds per repository

All repositories are public. All code is open source. There is no login wall, no token, no obfuscation. Visit the URL, read the README, clone if you want.

Repository owner: github.com/strulovitz

---

THE ARCHITECTURE — working code:

  github.com/strulovitz/GiantHoneyBee
    Coordinator-only hive variant. Simplest deployment.

  github.com/strulovitz/KillerBee
    Multi-VM hive cluster. Phase 3 deployed: 7 virtual machines on Linux,
    8-VM Debian-13 build in progress on a second physical host.
    Demonstrates the system running across multiple physical machines,
    coordinated by hierarchy, with no central operator and no global kill switch.

  github.com/strulovitz/WaggleDance
    LAN-scale orchestration infrastructure. Used for the cross-machine LAN
    test that proved the architecture works at multi-host scale.

  github.com/strulovitz/HoneycombOfAI
    Hive component repository.

  github.com/strulovitz/BeeSting
    Public-mode video-series project demonstrating the architecture at
    consumer-comprehensible scale. Includes the full strategic, outreach,
    and rule-file context for the project.

---

THE BOOKS — full text, public:

  github.com/strulovitz/MadHoney
    The full text of *MadHoney*. The threat-credibility book. This dossier
    is built around it. Tab 2 of this binder is the printed version.

  github.com/strulovitz/TheDistributedAIRevolution
    The original conceptual book. Foundational framing, pre-dates *MadHoney*.

---

THE PUBLIC DEMONSTRATION — videos and umbrella site:

  github.com/strulovitz/Honeymation
    Two complete public-mode explainer videos. Both on YouTube:
      youtube.com/watch?v=o8R58VuJFx8   (Private Mode for Organizations)
      youtube.com/watch?v=PTnAqZCAClw   (Public Mode for Everyone)

  github.com/strulovitz/BeehiveOfAI
    Public-domain umbrella site. beehiveofai.com — operational, HTTPS,
    Cloudflare-tunneled.

---

THE ACTIVIST RECORD — decade of attempts:

  github.com/strulovitz/BeeSting/blob/master/UNIVERSITY_LETTER_SENT_LOG.md
    Logged record of recent academic outreach attempts (Berkeley, Toronto,
    Montreal, MIT Physics, Stanford CS+EE) and their outcomes. Roughly 1,000
    sends in May 2026 alone. Ten years of earlier attempts in personal
    archives, available on request.

---

VERIFICATION INSTRUCTIONS FOR YOUR TECHNICAL TEAM:

  Step 1.  Visit github.com/strulovitz/KillerBee and read the README.
  Step 2.  Visit github.com/strulovitz/GiantHoneyBee and read the README.
  Step 3.  Watch the two videos (linked above) — total runtime under 30 minutes.
  Step 4.  Read MadHoney, in particular `chapter_10_the_proof.md` and
           `chapter_11_how_we_built_it.md`, for the proof and reproducibility
           specification.

  Total verification time: under 90 minutes for a competent reviewer.

  This is not Petals, not Exo, not LangChain, not CrewAI, not federated
  learning, not Ray Serve, not vLLM. The MadHoney book and the project
  READMEs explain why. If a reviewer dismisses the architecture without
  reading those pages, they have not done verification — they have done
  pattern-matching against a different reference class. Send it back to
  someone who actually read it.
