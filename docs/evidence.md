# Evidence Review

State of the research as of October 2026, and how it calibrates the simulation. Full references are in [references.bib](../references.bib). Speed-ups are written as time ratios: a 40% time reduction is 1/(1 − 0.40) = 1.67×.

---

## 1. Task level: controlled experiments

| Study | Setting | Design, N | Effect | Caveat |
|---|---|---|---|---|
| Noy & Zhang 2023, *Science* | Professional writing tasks | Online RCT, ~450 | Time −40% (1.67×), quality +18% | Short, self-contained tasks |
| Brynjolfsson, Li & Raymond 2025, *QJE* | Customer support | Staggered rollout, 5,172 agents | +15% issues resolved per hour; novices gained most, top agents almost nothing | One firm, one task type |
| Dell'Acqua et al. 2026, *Organization Science* | BCG consultants | RCT, 758 | Inside the frontier: +12% tasks, 25% faster (1.33×), quality +40%. Outside: 19 pp less likely to be correct | GPT-4 era |
| Peng et al. 2023, arXiv | Developers writing an HTTP server | Lab RCT, 95 | Time −56% (2.26×) | One toy task |
| Cui et al. 2025, *Management Science* | Developers at Microsoft, Accenture, a Fortune 100 firm | Three field RCTs, 4,867 | +26% completed tasks; juniors +27–39%, seniors +8–13% | Pull requests as output proxy |
| Dillon et al. 2025, arXiv | Office workers, Microsoft 365 Copilot | Field RCT, 7,137 | ~30 min/week less email, documents 12% faster, meetings unchanged | Workplace-wide gains are small |
| Schwarcz et al. 2025 | Law students, six legal tasks | RCT, ~130 | Productivity +34–140% in 5 of 6 tasks with reasoning or retrieval tools | Students, not practising lawyers |
| Becker et al. (METR) 2025, arXiv | Experienced open-source developers, real issues | RCT, 16 devs, 246 issues | **19% slower** with AI; developers believed they were 20% faster | Small N; early-2025 tools |
| METR 2026 redesign note | Same design, returning and new developers | RCT | Estimates near zero with wide intervals; METR calls the data too weak to size the effect | Selection: developers refused to work without AI |
| Otis et al. 2024, working paper | Kenyan entrepreneurs, GPT-4 mentor | RCT, 640, five months | Average ≈ 0; top performers +15%, weak performers −8% | Advice quality depends on the user's judgement |

**Reading.** On tasks inside the frontier, with a human in the loop, speed-ups cluster around 1.3–2.3×. A long right tail reaches ~5× on narrow, easily checked tasks. A meaningful minority of uses (10–25%) fall outside the frontier and cost time or accuracy. Gains are largest for less experienced workers.

No completed peer-reviewed RCT of autonomous agents in knowledge work existed at the time of writing. Several are registered.

## 2. Worker, firm and economy level

| Source | Finding |
|---|---|
| Humlum & Vestergaard 2025 (Denmark, 25,000 workers, 7,000 workplaces, register data) | Average time saved 2.8% of hours. No detectable effect on earnings or hours; effects above 1% ruled out. |
| Bick, Blandin & Deming 2026, *Management Science* (US representative surveys) | Users save 5.4% of work hours; about 1.4% of all hours economy-wide. |
| Anthropic 2025, "Estimating AI productivity gains from Claude conversations" | ~80% time savings per assisted task (≈5×) on 100,000 conversations; implies ~1.8 pp/year of US labour productivity growth over a decade. Model-estimated times, no counterfactual, excludes validation time outside the chat. |
| Acemoglu 2025, *Economic Policy* | At most ~0.66% TFP over ten years. |
| Penn Wharton Budget Model 2025 | +1.5% productivity level by 2035. |
| 2026 national statistics | Strong US productivity growth, but no causal attribution to AI yet. Executive surveys report larger gains than measurements find. |

**Reading.** Measured whole-worker effects in 2026 are a few percent: AP ≈ 1.03–1.06 among users, less across whole organisations. The distance between "5× per task" and "1.03× per worker" is Amdahl's law: the assisted tasks are a modest share of the job, AI is used on some of them, review takes time back, and freed time does not all become output.

## 3. How much work is exposed

- Eloundou et al. 2024, *Science*: about 80% of US workers have at least 10% of tasks exposed; about 19% have at least half.
- OpenAI GDPval 2025: on 1,320 well-specified tasks in 44 occupations, expert graders rated frontier model output as good as or better than the expert's on 41–48% of tasks.
- METR time horizons: the length of task that frontier models complete at 50% success has doubled roughly every 4–7 months; in early 2026 it was in the region of 12+ hours, with large uncertainty at the top end.

**Reading.** Exposure is broad and capability is rising fast. Realised use is far below exposure. This is the gap that the simulation's *adoption* and *reallocation* parameters represent, and E6 shows they move AP as much as model capability does.

## 4. Quality and failure modes

- Outside the frontier: −19 pp accuracy (Dell'Acqua), −8% revenue for weaker entrepreneurs (Otis), −19% speed for experts on their own codebases (METR 2025).
- "Workslop" (Niederhoffer, Hancock et al., *HBR* 2025, survey of 1,150): about 15% of received work is low-value AI output, costing nearly two hours per incident to deal with.
- Deskilling: endoscopists' unaided adenoma detection fell from 28.4% to 22.4% after AI was introduced (Budzyń et al. 2025, *Lancet Gastroenterology & Hepatology*; before/after design).

## 5. The 1.0 reference points, corrected

| 1.0 claim | What the sources say |
|---|---|
| Klarna 2022→2026: headcount −49%, revenue +104%, "AP ~3.5" | Klarna's own figures cover Q4 2022 to Q4 2025. 2.04 / 0.51 = 4.0, not 3.5; Klarna itself reports revenue per employee up 3.6×. It is revenue per head, which moves with prices, growth and outsourcing; in 2025 the CEO said the cost-driven AI push had produced "lower quality" and began a human-agent pilot. Not an AP measurement. |
| Meta "top engineer ~10×, per CTO" | Andrew Bosworth (Forbes, April 2026): his best engineer is "5x to 10x more productive" while spending roughly a salary on tokens. A self-reported anecdote. Jellyfish data: the top decile of engineers is ~2× the median while using ~10× the tokens. |
| Meta token leaderboard, "March 2026" | Reported April 2026 ("Claudeonomics", 85,000+ employees, shut down within days). The point stands: token counts are gamed the moment they are ranked. |
| AI-native SaaS €0.9–3.7M revenue per employee; pre-AI baseline €138–276K | Roughly right as SaaS benchmarks (private SaaS median ~$130–141K; Cursor > $5M per employee). Not a knowledge-work baseline and not an AP measure. |
| "Average EU knowledge-worker salary ~€62,000" | €62,235 is the **German** full-time mean (Destatis 2024). The EU full-time adjusted average is €39,800 (Eurostat 2024). Fully loaded German cost: ~€75–85K. |
| 200K tokens/day buys one extra AP (€16–€560/year) | No evidence links a token volume to an output quantity. Real heavy agentic use runs to millions of tokens per day; enterprise Claude Code users average ~$150–250 per month. See [economics.md](economics.md). |
| "Steam at 25–30% of the cost of horses by 1850", "~20× per steam engine" | No primary source found. Removed. |

## 6. Calibration used in the simulation

| Parameter | Typical 2026 | Integrated team | Agentic frontier | Evidence anchor |
|---|---|---|---|---|
| Exposure (share of a task AI can address) | 0.45 | 0.60 | 0.80 | Eloundou; GDPval |
| Adoption (share of tasks where it is used) | 0.40 | 0.65 | 0.90 | Bick et al.; Humlum & Vestergaard |
| Time saving when it works | 0.45 | 0.60 | 0.85 | Noy & Zhang; Dell'Acqua; Peng; Anthropic |
| Frontier miss rate | 0.15 | 0.12 | 0.10 | Dell'Acqua; METR; Otis |
| Review overhead (share of saved time) | 0.30 | 0.25 | 0.15 | Workslop; METR (assumption) |
| Reallocation of freed time | 0.50 | 0.70 | 0.85 | Humlum & Vestergaard (assumption) |
| Skill compression | saving ∝ baseline output^−0.35 | | | Brynjolfsson; Cui |

The typical scenario reproduces the measured economy-wide numbers: organisation AP-C ≈ 1.04 (time saved ≈ 4%) and AP-Q ≈ 1.02. That match is the check on the calibration; the other scenarios are extrapolations from it.

## Could not verify

Final page ranges for Dell'Acqua et al.; the exact novice effect in the published QJE version of Brynjolfsson et al.; the sign convention in METR's 2026 note (read via secondary sources); a reported 2026 Anthropic revision to ~1.0–1.2 pp/year; official 2026 GDPval figures; Klarna's exact 2025 year-end headcount.
