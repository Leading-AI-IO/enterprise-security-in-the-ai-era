# Where the Patch Ends — Reading Enterprise Security in the AI Era from the World’s Proposals

"The race to prevent intrusion is being lost to the attackers on speed. The only things a company can decide for itself are three: what to hold, when to notice and how to tell. And these three are the thinnest part of the world's proposals."

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Language](https://img.shields.io/badge/Language-Japanese%20%7C%20English-blue)](docs/)
[![Proposals](https://img.shields.io/badge/Proposals-211-informational)](data/proposals.csv)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--10--30-brightgreen)](https://github.com/Leading-AI-IO/enterprise-security-in-the-ai-era)

<p align="left">
  <img src="./assets/ogp_design.png" width="80%">
</p>

*他の言語で読む: [日本語](README.md)*

---

> **Definition**
>
> **This book**, by Satoshi Yamauchi (山内怜史), lines up the proposals on enterprise security in the
> AI era written in 2025–2026 by eight kinds of issuer — governments and public bodies, standards
> bodies, AI companies, security companies, insurers, academia, individual experts and regulators —
> **admitting only those whose primary source the author opened and verified in the text**, and from
> that ledger shows what a company can decide. It is an updatable book. The first edition (30 October
> 2026) holds 263 rows, of which 211 verified proposals are counted in the text (90 opened by the
> author, 121 opened at the author's instruction by an AI research assistant, which checked the
> wording and left the record in the ledger). Parts 1 and 2 assert
> nothing: they record, in the words of the primary sources, that attackers move in minutes while
> defenders move in days, that the issuers themselves wrote that their proposals are "not new", and
> that the stop-gap for the period when a fix is not in time was written into law without measured
> evidence, and they count where the 211 proposals agree, conflict and fall silent. Part 3 is where
> the author's claims begin: with no proposal's effect measured, the things that still mean something
> when the attack succeeds and that a company can decide without anyone's cooperation come down to
> three — **what to hold, when to notice and how to tell** — and these three are the thinnest part
> of the world's proposals. Part 4 follows those decisions through the decision to stop, the vendor
> contract, and the approval, the insurance and the board. The book does not say which measures
> prevent attacks, does not say AI caused the breaches, and makes no forecast; the conclusion sets
> out sixteen indicators to be recounted in the next edition. It is the companion to *The Japan
> Breach Registry 2026*, the ledger of facts.
>
> **Governance**: The author is the sole writer. One criterion admits a row into the count — the
> author opened the primary source and verified the wording (tiers T1 and T2); unverified rows stay
> in the ledger as T3 and are not counted. The claims from Part 3 onward are the author's and are
> kept apart from what the sources say. Primary sources are opened by the author; in edition 1, 121 rows
> were opened at the author's instruction by an AI research assistant (a sub-agent), which checked the
> wording and left the record in each row (Appendix A-3), so rows the author did not open directly can
> be told apart in the ledger. The author is not a security specialist but an AI strategist
> who has written on how AI changes business and organisations. Readers verify the ledger, report
> errors, and point to primary sources.
>
> *Author & full catalog: [github.com/Leading-AI-IO](https://github.com/Leading-AI-IO)*

---

## 📖 Overview

In the autumn of 2026, personal-data breaches were disclosed in Japan one after another. The author lined them up, one notice at a time and in the notices' own words, and published the ledger as the companion volume *The Japan Breach Registry 2026*. By its third edition it held 71 notices.

When the ledger was closed, one question remained. **Then what does a company decide?** All 71 organisations that wrote those notices had taken measures: multi-factor authentication, patching, vendor management. They were doing what the world's proposals say. They still leaked. And afterwards, what the company could write was "we suffered unauthorised access" and "we cannot rule out the possibility that data was leaked".

**This book collected the world's proposals in order to answer that question.**

### The proposal ledger

Proposals written in 2025–2026 by eight kinds of issuer were placed in the ledger `data/proposals.csv` only after the author opened the URL of the primary source and verified the wording in the text. The first edition holds 263 rows, of which 211 (non-merged rows in tiers T1 and T2) are counted. Each proposal is classified into one of nine kinds (K1–K9), and its correspondence to the intrusion vectors in the Japanese breach ledger is recorded row by row.

The proposals were then read with three questions: where they agree (Chapter 4), where they conflict (Chapter 5), and where they fall silent (Chapter 6). **Of the 211, fourteen are recorded as having a measured effect, and none meets this book's criterion (a measurement in companies' real environments comparing outcomes with and without the control). Data minimisation (K5) numbers thirteen including secondary classifications — the fewest of the nine kinds — and is written only by governments and public bodies and a single insurer.**

### The three things a company can decide

The answer lay in the silence. The proposals are thick on the side that prevents the attack: fixing vulnerabilities, multi-factor authentication, detection products. They are thin on the side that still means something after the attack has succeeded.

- **Hold less (Chapter 7)**: how much you hold sets the ceiling on what can leak
- **Notice (Chapter 8)**: whether records exist decides whether the actual leak can be narrowed below that ceiling. Only one proposal — India's CERT-In — states a log-retention period in days
- **Tell (Chapter 9)**: whether you can narrow it decides whether you notify quickly at the ceiling or notify after narrowing. Japan's 71 notices divide into 18 that gave the ceiling, 24 that narrowed from records, 14 that could not state a number and 15 that read either way

The three are not independent but a chain, and none of them is technology; each is a decision.

### Getting it through the company

What has been decided passes through three places inside the company: the decision to stop (Chapter 10 — Japan's Financial Services Agency and Bank of Japan asked top management for criteria set in advance, a proposal without parallel in the book's collection), the vendor contract (Chapter 11 — in Japan, companies with no such contract at all are the ones under supervision), and the approval, the insurance and the board (Chapter 12 — what passes is not evidence of effect but the company's own numbers). Part 4 adds no new decisions.

### What this book does not assert

The book does not say which measures prevent attacks; there is no source that measured it. It does not rest any proposal on the premise that "compensating defences can prevent attacks during the period when a fix is not possible". It does not say AI caused the breaches. It does not say Japan lags the world. It does not grade the organisations that wrote the notices. And it makes no forecast; forecasts belong in a separate ledger, *The AI Forecast Registry*.

---

## 📊 Ledger data

| File | Role | Contents |
| --- | --- | --- |
| [proposals.csv](./data/proposals.csv) | **Canonical** | The proposal ledger. 263 rows, 18 columns (UTF-8 with BOM). Column definitions in Appendix A-2, counting rules in Appendix A-4 |
| [count_proposals.py](./scripts/count_proposals.py) | Counting script | Recounts, from the canonical file, the indicators in the conclusion and the figures used in Chapters 4 and 6. Changes no file |

**Updates to this book are confined to three places**: the proposal ledger `data/proposals.csv`, Appendix B (the verification record) and the indicator table in the conclusion. Figures in the text refer to the "as of edition N" panel at the head of each chapter and to those three places; when the prose itself is changed, "(added/corrected on D Month YYYY)" is placed immediately before the change. Readers may open `data/proposals.csv` alone without reading the text.

---

## 📄 Documents

| File | Language | Contents |
| --- | --- | --- |
| [enterprise-security-in-the-ai-era_JP.md](./docs/jp/enterprise-security-in-the-ai-era_JP.md) | 🇯🇵 Japanese | Full text (Japanese). Introduction, four parts and twelve chapters, conclusion, Appendices A and B, 17 figures |
| [enterprise-security-in-the-ai-era_EN.md](./docs/en/enterprise-security-in-the-ai-era_EN.md) | 🇺🇸 English | Full text (English) |
| [UPDATE_RUNBOOK.md](./docs/UPDATE_RUNBOOK.md) | 🇯🇵 Japanese | Update runbook. The author is the sole writer of the ledger; the procedure is published |

---

## 🔄 Changelog

| Date | Version | Contents |
| --- | --- | --- |
| 2026-10-30 | v1.0 | First edition. Proposal ledger of 263 rows (211 counted, 39 in T3). Introduction, Chapters 1–12, conclusion, Appendices A and B. Japanese and English editions |
| 2026-10-30 | v1.0 (corrected) | Same-day corrections after publication. (1) The “effect measured” wording aligned with Chapter 6's breakdown (14 recorded, 0 meeting the book's criterion; Chapter 12, conclusion, two figures, Appendix A-4). (2) Opening records added to 121 T1/T2 rows; who opened them (author 90 / AI research assistant 121) stated in Appendices A-3 and B-3; six empty URLs filled. (3) “The numbers this chapter stands on” panels added to Chapters 7–12; table of contents added at the head of the text. No rows deleted, no tiers changed |

---

## 📑 Table of contents

- Introduction: The Question — What Remained After the Notices Were Lined Up
- **Part 1: Why It Cannot Be Prevented**
  - Chapter 1: The Speed Asymmetry — 29 Minutes and 43 Days
  - Chapter 2: Three Primary Sources That Wrote "Not New" — What AI Did Not Change
  - Chapter 3: Institutionalisation Without Evidence — How "Mitigation May Substitute" Became Rule
- **Part 2: A Map of the World's Proposals**
  - Chapter 4: Consensus — Every Proposal Eight Kinds of Issuers Agree On Predates AI
  - Chapter 5: Conflict — Fix Faster vs. Act on the Premise That You Cannot Fix
  - Chapter 6: Gaps — No Measured Effects, Thirteen on Data Minimisation
- **Part 3: The Three Things a Company Can Decide**
  - Chapter 7: Hold Less — The Only Way to Reduce Harm Whether or Not the Intrusion Succeeds
  - Chapter 8: Notice — Who Decides How Long Logs Are Kept?
  - Chapter 9: Tell — Who Decides How Many People to Notify?
- **Part 4: Getting It Through the Company**
  - Chapter 10: The Decision to Stop — Who Decides, and When?
  - Chapter 11: Vendors and the Reality of "No Contract" — Where in the Contract Are Your Decisions Written?
  - Chapter 12: Insurance, Ringi and the Board — Where Do Your Decisions Get Through?
- Conclusion: What to Count Again in the Next Edition
- Appendix A: Method — How We Collected, Verified and Counted
- Appendix B: Verification Record — Numbers We Could and Could Not Confirm

---

## 🔗 Related Projects

This book is connected to the following open-source projects.

| Project | Summary | Link |
| --- | --- | --- |
| **The AI Strategist**               | Defining the AI Strategist role with practical frameworks for the BTC intersection                              | [GitHub](https://github.com/Leading-AI-IO/the-ai-strategist)              |
| **Depth & Velocity**                | A methodology for new business development in the generative AI era                                             | [GitHub](https://github.com/Leading-AI-IO/depth-and-velocity)             |
| **The Silence of Intelligence**     | Systematizing Anthropic CEO Dario Amodei's philosophy — Industry Anatomy Series #2                              | [GitHub](https://github.com/Leading-AI-IO/the-silence-of-intelligence)    |
| **The Anatomy of Anthropic**        | A comprehensive dissection of Anthropic's strategy, products, research, and safety                              | [GitHub](https://github.com/Leading-AI-IO/the-anatomy-of-anthropic)       |
| **The Palantir Impact**             | Dissecting Palantir Foundry's ontology strategy — Industry Anatomy Series #1                                    | [GitHub](https://github.com/Leading-AI-IO/palantir-ontology-strategy)     |
| **What They Won't Teach You**       | What the AI-advantaged generation won't teach you about AI and the "Thinking OS"                                | [GitHub](https://github.com/Leading-AI-IO/what-they-wont-teach-you)       |
| **The Edge of Intelligence**        | When AI runs on your device: the end of cloud, the beginning of edge                                            | [GitHub](https://github.com/Leading-AI-IO/edge-ai-intelligence)           |
| **The Redesign of Design Strategy** | Redefining design strategy, including a structural analysis of IDEO's decline                                   | [GitHub](https://github.com/Leading-AI-IO/design-strategy-in-the-ai-era)  |
| **The Orchestrator**                | The first-ever definition of the rarest role in the AI era                                                      | [GitHub](https://github.com/Leading-AI-IO/the-orchestrator-in-the-ai-era) |
| **Advertising, Redesigned**         | An open-source book exploring the future of advertising in the AI era through strategic analysis of 7 companies | [GitHub](https://github.com/Leading-AI-IO/advertising-redesigned)         |
| **The AI Organization**             | The root cause of AI failure is not technology. Organizational theory for the AI era                            | [GitHub](https://github.com/Leading-AI-IO/the-ai-organization)  |
| **The Structural Shift from SaaS**  | SaaS Is Dead: The Structural Shift from SaaS to Service-as-a-Software                                           | [GitHub](https://github.com/Leading-AI-IO/saas-is-dead-the-next-ai-business-model)  |
| **The 10:80:10 Principle**          | The optimal balance for human-AI synergy:「10:80:10」in the AI era.                                             | [GitHub](https://github.com/Leading-AI-IO/the-10-80-10-principle)  |
| **A Trillion Dollars and a Firebomb** | The Parallel Realities of the AI Era | [GitHub](https://github.com/Leading-AI-IO/a-trillion-and-a-firebomb) |
| **The End of the Attention Economy** | The End of the Attention Economy. What Should the Next SNS Look Like? | [GitHub](https://github.com/Leading-AI-IO/the-attention-economy-is-over)  |
| **The Growth Engine of Anthropic** | Decoding the $1T Trajectory | [GitHub](https://github.com/Leading-AI-IO/the-growth-engine-of-anthropic)  |
| **The Agentic Commerce Economy** | When AI Agents Buy, the Advertising Model Paradigm Shift | [GitHub](https://github.com/Leading-AI-IO/agentic-commerce-economy)  |
| **Will ai break the planet** | The AI Infrastructure Boom and the Race Against the Climate's Point of No Return | [GitHub](https://github.com/Leading-AI-IO/will-ai-break-the-planet)  |
| **The-forward-deployed-shift** | The Forward Deployed Shift — Where Value Survives When "Building" Is Over | [GitHub](https://github.com/Leading-AI-IO/the-forward-deployed-shift)  |
| **Frontier-Grade Open Weights** | They Matched the Frontier. But No One Can Hold Them | [GitHub](https://github.com/Leading-AI-IO/frontier-grade-open-weights)  |
| **Earned-ai-model-optionality** | AI Models Are Switchable. But Only for Companies That Made Them So | [GitHub](https://github.com/Leading-AI-IO/earned-ai-model-optionality)  |
| **Us-china-ai-competition** | The Layers of US-China AI Competition — What is being decided is not who is stronger, but who writes the terms | [GitHub](https://github.com/Leading-AI-IO/us-china-ai-competition)  |
| **The China AI Registry** | The five Chinese AI models you can name are under 1% of the ones China counts | [GitHub](https://github.com/Leading-AI-IO/the-china-ai-registry)  |
| **The AI Forecast Registry** | The AI Forecast Registry — Recording What Was Predicted, Before It Resolves | [GitHub](https://github.com/Leading-AI-IO/the-ai-forecast-registry)  |
| **Enterprise Security in The AI Era** | Where the Patch Ends — Reading Enterprise Security in the AI Era from the World’s Proposals | [GitHub](https://github.com/Leading-AI-IO/enterprise-security-in-the-ai-era)  |

For other books, see [github.com/Leading-AI-IO](https://github.com/Leading-AI-IO).

---

## 👤 Author

**Satoshi Yamauchi** (山内 怜史)

* **AI Strategist & Business Designer at Sun Asterisk Inc.**
* **Founder / AI Strategist at [Leading.AI](https://www.leading-ai.io/)**
* Over fifteen years crossing the three domains of Business, Technology and Creative. Led 40 projects as PL/PM as an IT consultant at Future Architect, then worked in business strategy and new-business development at Recruit. At Sun Asterisk, as Business Designer and AI Strategist, systematised "Depth & Velocity", a methodology for new-business development with generative AI.
* This project is part of the research by Leading.AI.
* [📒 Read my insights on Note](https://note.com/satoshi_yamauchi)
* [🌐 Visit Leading.AI Official Website](https://www.leading-ai.io/)

---

## 🤝 Contributing

**This book does not accept Pull Requests.** The author is the sole writer of the ledger, and this is part of the book's design. The discipline that only someone who has opened the primary source assigns a tier and replaces the proposal's wording with the words of the text wavers as the number of writers grows. A ledger that wavers cannot be used for verification.

Issues are welcome. Two kinds are accepted.

**① Reports of errors.** A proposal's wording does not match the primary source. A tier (T1–T3) or kind (K1–K9) does not fit what the source says. A date is wrong. A URL does not resolve. A figure in the text does not match the ledger. The author checks against the primary source and, if it is an error, appends a correction. **The original row is never deleted.** The name of the person who reported it is recorded in the row or in Appendix B.

**② The location of primary sources.** For the 39 rows held outside the count as T3, information from anyone who knows a URL that reaches the primary source's text is welcome. The author opens it, verifies the wording and upgrades the row to T1 or T2. **Every row that meets the criterion is counted, without exception.**

Issues that include a verdict that "this measure works" or "does not work" are accepted for that part only when accompanied by the location of a primary source that measured the effect. The book records only what the primary sources say.

In particular, information is welcome on the following, which the author had not been able to verify as of the first edition (Appendix A-7):

- The text of CISA Binding Operational Directive 26-04 (currently relying on CISA's announcement, FedRAMP's primary material and third-party commentary)
- The Mandiant M-Trends 2026 report itself (currently relying on the announcement article)
- The location on EUR-Lex of the text of Article 23 of the EU NIS2 Directive (the first edition verified only Recital 102 on EUR-Lex)
- Primary sources in the names of individual Japanese experts (contributed articles, lecture records, testimony)

---

## 📝 License

This book is published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). With attribution, it may be freely quoted, reproduced and adapted.

Copyright (c) 2026 Leading.AI
