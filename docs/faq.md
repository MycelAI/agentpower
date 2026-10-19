# Frequently Asked Questions

## The concept

**Why a new unit? Isn't revenue per employee enough?**

Revenue per employee moves with prices, growth, product mix and outsourcing. In the simulation it ranked organisations' true AP with a correlation of only 0.26 and overstated gains 2.5-fold. Agentpower isolates one question: how much more value does each FTE deliver than the same role did without AI?

**Isn't this just productivity with a new name?**

It is a specific, auditable productivity ratio for one cause and one kind of work. "Productivity" covers everything; "AP-Q 1.14 [1.02–1.27] for claims handling" says what changed, by how much and how sure we are.

**How is it different from FTE-equivalents?**

FTE counts capacity you pay for. AP counts output you get per unit of it. A 20-FTE team at AP-Q 1.25 delivers what 25 FTE did before.

**Why did the typical AP ratio fall from 3–10 to about 1.05?**

Because 1.0 read task-level speed-ups as job-level ones. AI often makes a single task two to five times faster. But a job is many tasks, AI is used on some of them, checking takes time back, and saved time doesn't all become output. Amdahl's law does the rest: to reach AP 3, AI must remove two thirds of a role's working time and every minute of it must be reused. The best population studies find 3–5% of hours saved. See [evidence.md](evidence.md).

**So is AI overhyped?**

No. A team at AP 1.3 delivers 30% more with the same people, and an extra AP still costs two to five times less through AI than through hiring. Agentic frontier teams in the simulation reach 1.5–2. Capabilities are compounding quickly. The point of a unit is to see the change as it happens, not to assume it.

## Measurement

**How do you actually measure it?**

Count effort-weighted deliverables per FTE, have a blind panel score a random sample for value, and compare with a baseline and ideally a control group (AP-Q). Separately, time a sample of tasks with and without AI to get capacity (AP-C). The protocol is in [measurement.md](measurement.md); a worksheet is in [ap-calculator.md](../examples/ap-calculator.md).

**Why not just ask managers?**

People overestimate. In the METR 2025 trial, experienced developers believed AI made them 20% faster when it made them 19% slower. In the simulation, manager estimates overstated the gain 3.4-fold.

**Why not use token consumption? It's easy to measure.**

Tokens per unit of work vary a hundredfold between models and working styles, and token counts are gamed as soon as they are ranked. Meta's internal "Claudeonomics" leaderboard (April 2026) was shut within days. In simulation, the 1.0 token conversion overstated gains more than a hundredfold and almost tripled when gamed.

**Isn't quality subjective?**

Partly, which is why the audit is blind, uses a fixed rubric per role, and compares samples from both periods scored by the same reviewers. It is less subjective than assuming quality holds.

**How precise is it?**

For one team in one period, about ±12% with 80 audited deliverables and effort-weighted counts. You can tell 1.0 from 1.3, not 1.05 from 1.10. Pool teams or periods for finer distinctions.

**Can it be gamed?**

Every metric can. AP-Q moved +8% under the simulated gaming incentive, against +40% for raw counts and +184% for tokens, because splitting work lowers each item's audited value. Keep reviewers blind and rotate them.

**Can AP be below 1?**

Yes, and it should be reported when it is. Outside the "jagged frontier" AI costs time and accuracy. About 15% of individual workers in a typical 2026 organisation end up below 1.0 in the simulation.

## Implications

**Does a high AP ratio mean fewer jobs?**

Not necessarily. It means more output per FTE. Whether that becomes more output or fewer people depends on demand and on choices organisations make. The Danish register study found no effect on earnings or hours so far. Transitions are still painful for the people they displace, and institutions carry responsibility for them.

**Is this only for large companies?**

No. A small team can run the protocol on one role in two weeks. The advantage of amplification goes to whoever turns saved time into value, which is a question of management more than of size.

**What about professions where human presence is the product?**

Therapy, surgery, nursing, teaching young children: AP applies to their cognitive components only (documentation, planning, research). A therapist with faster notes isn't seeing more patients with less attention; they are spending more of the hour with the person in front of them.

## The term

**Why "agent"?**

It bridges both eras: the human agents whose work is being amplified (lawyers, brokers, administrators) and the AI agents doing the amplifying. From Latin *agere*, to act.

**One word or two?**

One word, lowercase in running text, abbreviated AP, following "horsepower".

**Is it trademarked?**

No. The word and the ideas are free for anyone to use. The text is CC BY-SA 4.0 and the code is MIT.
