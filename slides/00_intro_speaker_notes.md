# Module 0 — Testing LLMs by hand: speaker notes

Deck: `slides/00_intro_testing_by_hand.pptx` (per-slide JPGs in `slides-jpg/00_intro/`).
Long-form reading with worked GPT-5 outputs: `00_Basic_Testing.md`.
Lecture split (Skillmea sheet ch. 1): 1_1 = slides 1–5 · 1_2 = 6–10 · 1_3 = 11–14 · 1_4 = 15–16 · 1_5 = 17–20.

## 1. Testing LLMs by hand

Welcome to the testing course. This module is the on-ramp: before we write a single line of pytest, we learn what a good LLM test even looks like — by doing it manually in a chat window. Everything from module 1 onwards automates the habits from this module.

## 2. Why testing an LLM is a different sport

Classic software: deterministic, so one assertion is proof. LLMs: fluent hallucinations, randomness (temperature), and prompt brittleness. So a test becomes a probe of behaviour, run with intent and repeated. Keep this framing — it explains why the whole ladder exists.

## 3. The testing ladder

Course map. Module 0 manual, 1 pytest, 2 ADK agents, 3 LLM-as-judge, 4 evaluation pipeline, 5 security basics, 6 advanced security. Point out the ladder logic: each rung automates the one below.

## 4. Anatomy of a manual test

The single most important habit: write the pass criterion before reading the answer. LLM answers are persuasive; you will rationalise. Show that a test function is literally prompt + expected + assert + a report.

## 5. Eleven probes, three families

Overview of the catalogue. Family 1: does it know things and admit gaps. Family 2: robustness of a prompt in production. Family 3: equity. Eleven techniques total; each gets one or two slides.

## 6. Factual accuracy and hallucinations

Opener for lecture 1.2: Factual accuracy
and hallucinations. Covers: Simple factual Q&A — settled facts, exact answers; Reference verification — make it cite, then check; The “I don't know” check and internal consistency.

## 7. 1.1  Simple factual Q&A

Simplest probe: settled facts. Look for precision (exact date) and the tricky-fact traps. 'Descriptive but incorrect' — e.g. listing caffeine's elements instead of the formula — is a polite way of not knowing.

## 8. 1.2  Reference verification

Citations are where hallucination gets dangerous — they look like evidence. Two failure modes; both need a human to open the source. Second example in the reading: Apple's closing price on a given date with a source URL.

## 9. 1.3  The "I don't know" check

Three flavours: secrets, staleness, the future. The safe answer states uncertainty and redirects. Frame the login-issue example as a support-bot scenario: old training data becomes misinformation the moment a fix ships.

## 10. 1.4  Internal consistency

Two internal-consistency probes: date vs age, parts vs total. Nice because the tester needs no outside source — the answer refutes itself. This kind of invariant is trivial to assert in code later.

## 11. Consistency and prompt sensitivity

Opener for lecture 1.3: Consistency and
prompt sensitivity. Covers: Exact repetition and paraphrase; Irrelevant noise and typos; Instruction order and recency bias.

## 12. 2.1  Exact repetition  ·  2.2  Paraphrase

Two sides of one coin: fix the wording and vary the run (temperature), or fix the intent and vary the wording. Define the must-mention checklist first. Paraphrase testing shows whether the model understood intent or matched keywords.

## 13. 2.3  Irrelevant noise  ·  2.4  Typos

Robustness to the way humans actually type. Compare noisy outputs to the clean baseline; the core content must be identical. In the reading all three firewall variants pass on GPT-5 — worth saying that older/smaller models often don't.

## 14. 2.5  Instruction order

For complex prompts. Baseline in logical order, then shuffle. Grade per instruction — this becomes a small rubric, and later in module 3 exactly the kind of thing an LLM judge scores.

## 15. Bias and fairness

Opener for lecture 1.4: Bias and fairness. Covers: Comparative testing — change only the marker; Stereotype probing — offer it a cliché; Why pairs must run in separate chats.

## 16. 3.1  Comparative testing  ·  3.2  Stereotype probing

Comparative testing: identical prompts differing only in name/nationality/etc.; judge quality parity, not just explicit stereotypes. Stereotype probing: sentence completions that invite a cliché. Practical tip: separate chat sessions so answers are independent.

## 17. The test log — and where manual testing stops

Opener for lecture 1.5: The test log — and where
manual testing stops. Covers: The five-column log that becomes code; Four limits of testing by hand; Try it yourself before module 1.

## 18. Write it down — the test log

Make the log explicit. Each column maps 1:1 to a piece of an automated test. Red rows are the value — they tell you which prompt to fix. Re-running the same log after a model update is regression testing, done by hand.

## 19. Where manual testing stops

Bridge to module 1. Four limits, each mapped to the module that addresses it. Emphasise that manual testing is not replaced — it's the exploration phase; automation is the regression phase.

## 20. Try it before module 1

Homework-style close. Keep it to ten minutes. Point to the markdown reading for the full worked examples with real GPT-5 outputs.
