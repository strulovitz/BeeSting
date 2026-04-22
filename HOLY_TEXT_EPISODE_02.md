# Holy Text — Episode 2 (AI Companies, Chapter 1)

**Locked narration. Word-for-word. ElevenLabs Frank voice.**
**Drafted:** 2026-04-22
**Source chapter:** `MadHoney/chapter_01.md`
**Target length:** ~13 minutes.

---

## Block 1 — The iceberg's tip (~30 seconds)

Twenty dollars a month. Two hundred dollars a month. Twenty, twenty, twenty. ChatGPT Plus. ChatGPT Pro. Claude. Gemini. Grok. The industry collects fifty-five billion dollars a year on those monthly receipts. And after collecting every last one of them, OpenAI is still not profitable — they burn through eight billion dollars a year in compute, and they are not projected to make money until 2030. Anthropic hit thirty billion dollars in annual revenue and is still burning cash.

How does the industry survive?

The subscription is not what pays for the industry. The subscription is the tip of the iceberg. The part above the waterline. The part you can see.

Everything that makes this industry actually valuable is below.

---

## Block 2 — The part below the waterline (~3 minutes)

When you type a question into ChatGPT, you are not the customer. You are the product.

Every question you have ever asked one of these systems is stored. Your IP address is attached. Your account. Your device fingerprint. The time of day. The session before, the session after. Every word you have ever typed — medical, legal, sexual, financial, psychological, criminal — sits in their logs, indexed, searchable, linked to you.

Every time you typed "am I showing early signs of pancreatic cancer."

Every time you typed "how do I leave my husband."

Every time you typed "what are the penalties for tax fraud in California."

Every time you typed "my daughter has been cutting herself."

Every time you typed "my wife is having an affair with my brother."

Every time you typed "can my employer fire me for being gay."

Every time you typed "how do I handle a mistress threatening to tell my wife."

Every time you typed "how much OxyContin is too much."

All of it stored. All of it indexed. All of it available to be sold.

They tell you it is anonymized. That is a lie. A single question that mentions your wife's first name, your daughter's school district, your employer, and your specific medical condition identifies you more precisely than your social security number ever has. Stripping your name from a record that contains a hundred other identifiers is not anonymization. It is theater. Software exists today whose entire function is to re-identify so-called anonymized records in under two seconds each. Hospitals buy it. Insurance companies buy it. Governments buy it. The research on re-identification has been settled for twenty years. Eighty-seven percent of Americans can be uniquely identified using only their five-digit zip code, their birthdate, and their sex. A conversation with ChatGPT contains thousands of data points stronger than those three.

Who buys your re-identified conversations?

The National Security Agency buys it. Not directly — indirectly, through contractor intermediaries that exist precisely to launder the transaction. That is the Snowden pattern. That is the pattern that has been documented for a decade.

Insurance companies buy it. The person who searched "early signs of pancreatic cancer" three months ago is a person whose premiums quietly rise at their next renewal — before they ever see a doctor, before they have a diagnosis, before they know anything is wrong.

Marketers buy it. The person who searched "how to tell if my husband is gay" is a person who can be sold to at the right emotional moment by the right advertiser — divorce attorneys, dating services, therapists, reputation-management firms.

Employers buy it. The person who asked ChatGPT about depression symptoms last year is a person who will not get the promotion they applied for this year. Nobody will tell them that is why.

Extortionists buy it on the dark web. The person who searched "how do I handle my mistress threatening to tell my wife" is a person with a direct price tag already calculated — the dollar amount their silence is worth to them. Whoever pays for that record collects it.

Facebook's subscription revenue is zero dollars. Facebook's data revenue is one hundred and thirty-four billion dollars a year. ChatGPT has ten times the intimate data per user that Facebook has ever had. Do the arithmetic. Eight billion of compute against one billion of ad revenue does not close unless there is a third revenue line nobody mentions on the earnings call.

That third line is you.

The subscription pays the compute bill. The data pays everything else — and the data is the part that makes the industry actually valuable. The subscription is the anchor customer. The data is the dividend.

Now let us talk about who replaces them.

---

## Block 3 — The price table (~60 seconds)

DeepSeek — a Chinese model, open-weight, free to self-host — is ninety-six percent cheaper than GPT-4o on every API benchmark they chose to publish.

Qwen, from Alibaba — open-weight, free to self-host — is ten to seventeen times cheaper than Claude Opus.

Kimi, from Moonshot AI — open-weight, free to self-host — was designed, in their own stated words, to "destroy current high-end API pricing structures."

Those are the ceiling prices. The API prices. The prices that include a company's server costs, salaries, and profit margin.

On your own hardware, the cost is zero. Just electricity.

Now stack those free Chinese models inside a hierarchical hive. A RajaBee at the top. GiantQueens below. DwarfQueens below them. Workers at the bottom. Each level runs a complete AI model. Every level free. Every model free. Every machine is one that somebody already owns.

You are not competing with DeepSeek. You are competing with free. You cannot win that competition.

---

## Block 4 — Mechanism I: the Attention Deficit of Centralized AI (~3 minutes)

Here is the architectural reason you cannot win it, even if you kept your prices.

Your centralized AI — GPT-5, Claude Opus, Gemini Ultra, whatever the latest one is called — has one brain. One context window. One thread of thought. No matter how large that brain is, it has to choose. It skims. It prioritizes. It decides what looks relevant and ignores the rest.

This is the Attention Deficit of Centralized AI.

In the nineteen-nineties, a chess grandmaster was asked how a human can compete against a computer that evaluates thousands of moves per second. He answered: "Yes, but in those same seconds, I only think about the heart of the matter — the most relevant part."

For decades that was considered the human advantage. Focus on what matters. Ignore the noise.

Then, in twenty-sixteen, something broke that assumption forever.

Google's AlphaGo was playing the ancient game of Go against Lee Sedol, one of the greatest living players. In the second game of the match, AlphaGo made a move. Move thirty-seven. A shoulder hit on the fifth line. Every human expert watching the match dismissed it as a mistake. Commentators estimated that a human would play that move once in every ten thousand games. Lee Sedol was so stunned he left the room for fifteen minutes.

Move thirty-seven was not a mistake. Move thirty-seven won the game. It influenced the center of the board in a way no human player had ever considered.

The lesson is devastating for centralized AI: the branches that look irrelevant at first are sometimes the branches that matter most. A centralized AI — no matter how much money you spent on it — must decide which branches to explore and which to prune. It will always miss the Move thirty-sevens. The one-in-ten-thousand insights that hide in the branches it chose not to look at.

Our system does not have this problem.

In our system, the DwarfQueen splits the question into independent branches. Each Worker takes one branch and gives it full attention. Unlimited time. Unlimited depth. Complete focus. A Worker analyzing an edge case that seems unlikely gives that edge case the same thoroughness that another Worker gives to the obvious scenario. Nothing is skimmed. Nothing is pruned. Nothing is dismissed as "probably not relevant."

And because all the Workers run in parallel, this thoroughness costs no extra time. A hundred Workers analyzing a hundred branches in parallel take the same wall-clock time as one Worker analyzing one branch.

No Move thirty-seven is ever missed. Because no branch is ever pruned.

You cannot fix this by making your single model bigger. You can only fix it by making it a swarm.

And a swarm is what my system is.

---

## Block 5 — Mechanism II: train once, copy forever (~90 seconds)

Now add customization.

Fine-tuning a closed model through OpenAI's API costs twenty-five dollars per million training tokens — and that is before you pay to actually use the fine-tuned model. On Azure, it is around one hundred dollars per hour of training time.

With our system, you download an open-weight model. You fine-tune it on your own hardware. The cost is electricity. And once you have trained it, you copy it. You replicate that fine-tuned specialist across ten Workers, one hundred Workers, a thousand Workers. Every copy is free. Every copy is identical. Every copy runs independently.

A hospital trains a model to be an expert in its own radiology. A law firm trains a model to be an expert in its own contract language. A manufacturer trains a model on its own production line. Then they copy the specialist across every Worker in their hive.

Train once. Copy forever.

There is a community of people who do this for fun. On HuggingFace, the world's largest open model repository, names like Bartowski, Unsloth, and Mradermacher upload optimized versions of new foundation models within hours of their release. They do it for free. They give the work away. The models they produce run on graphics cards that hundreds of millions of people already own.

You cannot take ChatGPT and train it for your own use case. You take what they give you, or you leave. With our system, you own the specialist, you copy the specialist, and the specialist gets better every iteration.

---

## Block 6 — The OpenClaw closer (~2 minutes)

One more piece of evidence, and then the equation.

Peter Steinberger built ClawdBot — a small open-source tool that connected to Anthropic's Claude API. It became massively popular. Anthropic's response was a textbook case of what the industry calls Platform Squeeze.

Step one — the rebrand. Anthropic threatened legal action over the name. ClawdBot became Moltbot, then OpenClaw.

Step two — the OAuth cut. Anthropic disabled third-party OAuth access for consumer subscriptions. OpenClaw users were forced off their twenty-dollar-a-month plans and onto pay-per-token API billing. Ten to fifty times more expensive, overnight.

Step three — the absorption. Anthropic quietly added OpenClaw's core features — persistent memory, task automation — into their own Claude Code product.

Step four — the ban. On April fourth, twenty-twenty-six, Anthropic formally banned third-party "non-official harnesses" from using subscription tokens at all.

And then, the part that tells you everything.

In February twenty-twenty-six, OpenAI hired Peter Steinberger. Not because they needed his software — his software was free. They needed him. Under their roof. Under their control. Because a person who disrupts your business once will disrupt it again, and the second disruption is always worse than the first.

The software was free. The insurance policy was not.

Matt Schlicht built Moltbook. Meta bought him almost immediately. Same reason. Not the software — him.

This is the precedent. The industry understands exactly how to handle a rogue inventor who threatens its revenue model. Pay him, bring him in, prevent the next thing he builds.

I am the next Steinberger.

The scale of the disruption is not a tool that wraps your API. The scale of the disruption is the replacement of your entire business model — subscription and data — by a free system that runs on hardware people already own.

The payment is simpler than Steinberger's. I do not want employment. I want one wire, once, to banks you do not control, in jurisdictions your lawyers do not reach. That is the price. That is the whole offer.

---

## Block 7 — Death spiral (~45 seconds)

OpenAI is already placing advertisements inside ChatGPT. The sponsored-recommendation line at the bottom of conversations. A partnership with Criteo. A two-hundred-thousand-dollar minimum spend for advertisers. They project one billion dollars in ad revenue in twenty-twenty-six.

One billion of ad revenue against eight billion of compute cost. The arithmetic does not close.

When the most successful AI company in the world resorts to advertising, it tells you the subscription model alone cannot sustain the infrastructure. Ads annoy users. Users leave. Fewer users means fewer impressions. Advertisers pay less. Revenue drops further. Compute costs do not drop, because the 1.4 trillion dollar infrastructure commitment is already signed.

This is a death spiral. It has already begun.

---

## Block 8 — The replacement trigger (~90 seconds)

On January twenty-seventh, twenty-twenty-five, DeepSeek released a single model. In one day, Nvidia lost six hundred billion dollars in market value. The largest single-day loss in American stock market history. The entire Nasdaq dropped three percent. The entire semiconductor sector crashed.

That was one model. One afternoon. One news cycle.

The Chinese stack is already ahead on cost. Already matching on capability for most tasks. The world's largest AI compute base — one-point-four billion Chinese citizens, hundreds of millions of household computers, electricity Chinese citizens already pay for — is already in place. The missing piece is the coordination layer that stacks all of it into a single global hierarchical mega-hive.

That piece is on my GitHub.

It is free.

The day one Chinese engineer stitches DeepSeek together with the hive and releases it for mass distribution, the replacement begins. That engineer is not blocked by anything any American institution controls. When that day arrives, the world stops paying OpenAI and Anthropic for AI. The world starts paying DeepSeek, Alibaba, and Moonshot. America does not lose its AI lead gradually over a decade. America is replaced in months.

The only variable is whether that day arrives before this warning is paid out, or after.

---

## Block 9 — Closing equations (~15 seconds)

America's AI leadership equals your call.

Do nothing — China rules.

Forward this — America fights back.

---

## Block 10 — End card (silent, ~5 seconds)

`YouTube: Nir Strulovitz`
`github.com/strulovitz`

Final music note. Cut to black.

---

## Voice / delivery notes

- Same Frank voice as Episode 1. Series continuity is more important than voice variety.
- Block 2 (the data-harvesting catalogue) is the tonal peak of the episode. The list of questions — cancer, husband, cutting, affair, gay, mistress, OxyContin — should be read with *slowing* cadence, not speeding. Each one is a scalpel. The list is the evidence. Let it land.
- The seven named questions in Block 2 are intentionally constructed to span the taxonomy of what the industry actually harvests: health, family collapse, self-harm, infidelity, sexuality, extortion exposure, addiction. Do not cut them down for time. They are the block.
- Block 4 (Move 37) is the Kurzgesagt centerpiece visually. The narration is lighter there on purpose — the visuals do the work. Narrator does not oversell.
- Block 6 (OpenClaw) must read as a four-step mechanical sequence, not a story. The steps are the point. Each "Step one / step two / step three / step four" is its own beat.
- Block 9 closing equations: same cadence as Episode 1. Three lines. Equal weight. No rising intonation on any of them.
