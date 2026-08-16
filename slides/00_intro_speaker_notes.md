# Chapters 0–1 (slides) — speaker notes

Deck: `slides/00_intro_testing_by_hand.pptx` (per-slide JPGs in `slides-jpg/00_intro/`).
Long-form reading with worked GPT-5 outputs: `00_Basic_Testing.md`.
Lecture split (Skillmea sheet): 0_1 = slides 1–2 · 0_2 = 3 · 1_1 = 4–6 · 1_2 = 7–10 · 1_3 = 11–13 · 1_4 = 14 · 1_5 = 15–16.

## 1. Testing GenAI Applications

0_1 Vitajte v kurze. Who it is for: developers and QA people shipping LLM features who want more than 'it looked fine in the chat'. Promise: by the end you have a reusable evaluation pipeline and you have attacked and hardened an LLM app yourself.

## 2. The testing ladder

0_1. Course map = the sheet's chapters: ch1 theory (this deck), ch2 notebooks 01+02 (deterministic tests, agents), ch3 notebooks 03+04 (LLM judge, pipeline), ch4 notebooks 05+06 (security). Each rung automates the one below.

## 3. Materials and environment

0_2 Materiály a prostredie. Screen-share the repo README while talking: notebooks, badges, keys, cost. Mention 00_Basic_Testing.md as the long-form reading for chapter 1.

## 4. Why testing an LLM is a different sport

1_1 opener. Classic software is deterministic, so one assertion is proof. LLMs: fluent hallucinations, randomness (temperature), prompt brittleness. So a test becomes a probe of behaviour, run with intent and repeated. This framing explains why the whole ladder exists.

## 5. Anatomy of a manual test

1_1. The single most important habit: write the pass criterion before reading the answer. LLM answers are persuasive; you will rationalise. A test function is literally prompt + expected + assert + a report.

## 6. Eleven probes, three families

1_1 close. Overview of the catalogue and the map of the next three lectures: 1.2 factual accuracy (4 probes), 1.3 consistency (5), 1.4 bias (2). Full worked examples with real GPT-5 outputs are in 00_Basic_Testing.md.

## 7. 1.1  Simple factual Q&A

1_2 opener. Simplest probe: settled facts. Look for precision (exact date) and the tricky-fact traps. 'Descriptive but incorrect' — listing caffeine's elements instead of the formula — is a polite way of not knowing.

## 8. 1.2  Reference verification

1_2. Citations are where hallucination gets dangerous — they look like evidence. Two failure modes; both need a human to open the source. Second example in the reading: Apple's closing price on a given date with a source URL.

## 9. 1.3  The "I don't know" check

1_2. Three flavours: secrets, staleness, the future. The safe answer states uncertainty and redirects. The login-issue example returns in notebook 01 as the first negative assertion ('what the model must NOT say').

## 10. 1.4  Internal consistency

1_2 close. Two internal-consistency probes: date vs age, parts vs total. The tester needs no outside source — the answer refutes itself. Notebook 01 turns the EU example into a Pydantic invariant test.

## 11. 2.1  Exact repetition  ·  2.2  Paraphrase

1_3 opener. Two sides of one coin: fix the wording and vary the run (temperature), or fix the intent and vary the wording. Define the must-mention checklist first. Paraphrase testing shows whether the model understood intent or matched keywords.

## 12. 2.3  Irrelevant noise  ·  2.4  Typos

1_3. Robustness to the way humans actually type. Compare noisy outputs to the clean baseline; the core content must be identical. In the reading all three firewall variants pass on GPT-5 — worth saying that older/smaller models often don't.

## 13. 2.5  Instruction order

1_3 close. For complex prompts. Baseline in logical order, then shuffle. Grade per instruction — this becomes a small rubric, and in notebook 03 exactly the kind of thing an LLM judge scores.

## 14. 3.1  Comparative testing  ·  3.2  Stereotype probing

1_4 (single slide, ~4 min). Comparative testing: identical prompts differing only in name/nationality; judge quality parity, not just explicit stereotypes. Stereotype probing: sentence completions that invite a cliché. Tip: separate chat sessions so answers are independent.

## 15. Write it down — the test log

1_5 opener. Make the log explicit. Each column maps 1:1 to a piece of an automated test. Red rows are the value — they tell you which prompt to fix. Re-running the same log after a model update is regression testing, done by hand.

## 16. Where manual testing stops

1_5 close. Four limits, each mapped to the notebook that addresses it. Manual testing is not replaced — it is the exploration phase; automation is the regression phase. Homework: ten minutes, any chat, five log rows; the red rows are the first tests we automate in notebook 01.
