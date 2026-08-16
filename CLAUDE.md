# testing-tutorial — Testing GenAI Applications

Hands-on LLM-testing course: a "testing ladder" from manual probing (Module 0) to
adversarial security testing (Modules 5–6). Companion to the EU AI Act for Developers
course (Article 15). Registry slug `testing-genai`; the whole repo syncs to the Courses
drive folder `7. Testing GenAI (SYNCED)/course_materials (shared)` via `drive-push`.

## Layout

| Path | What |
|---|---|
| `slides/00_intro_testing_by_hand.pptx` | Chapters 0–1 deck (16 slides; each slide's kicker = sheet lecture code 0_1…1_5; speaker notes inside). Built by `slides/build_00_intro.py` — edit the script, not the pptx. |
| `slides/00_intro_speaker_notes.md` | Notes exported from the deck for reading while filming (`python3 slides/export_notes.py`). |
| `slides-jpg/00_intro/` | Per-slide 1920px JPGs (Robert's voiceover workflow). Regenerate: `pdftoppm -r 192 -jpeg -jpegopt quality=90 slides/00_intro_testing_by_hand.pdf slides-jpg/00_intro/slide` |
| `00_Basic_Testing.md` | Long-form Module 0 reading with worked ChatGPT outputs. Keep — the deck summarises it, does not replace it. |
| `01`–`06` notebooks | Executed WITH outputs + Colab badges (hub CLAUDE.md tutorial-notebook convention). |

## Models & keys

- Notebooks 01–04: OpenAI Responses API (`client.responses.create/parse`), model
  `OPENAI_MODEL = "gpt-5.6-luna"` (cheapest current OpenAI model, Aug 2026; `gpt-5-nano`
  retires 2026-12-11). nb02 routes it through ADK's `LiteLlm("openai/<model>")`.
- Notebooks 05–06: OpenRouter (openai SDK with `base_url`), roster: `anthropic/claude-sonnet-5`,
  `openai/gpt-5-mini`, `google/gemini-3.5-flash`, `deepseek/deepseek-v3.2`,
  `mistralai/mistral-small-2603` (display name "Mistral Small 4"). Whenever this roster
  changes, re-sync `ai-act-developers-course` M05 slide 7 + notes.
- Keys: `OPENAI_API_KEY` in `~/.config/training-ops/openai.env`; `OPENROUTER_API_KEY` in the
  gitignored local `.env`. Load both before running: `set -a; . ~/.config/training-ops/openai.env; . .env; set +a`.
- venv: `.venv` (py3.12, full stack incl. google-adk, jupyter). In notebooks use
  `!{sys.executable} -m pytest` / `%pip` — never bare `!pytest`/`!pip` (headless nbconvert has no
  `python`/`pytest` on PATH here).

## Refresh outputs

```
.venv/bin/jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=1800 0X_*.ipynb
```
Notebooks 01–04 can run in parallel (no shared output files). After executing, grep the
.ipynb files for local paths (`scratchpad`, `/private/tmp`, `.venv`) — nothing may leak.
`test_*.py`, `exercise_2.py`, `report.html` are notebook write-outs and gitignored.

## Slides design rules

Same language as Robert's other decks (see `training-ops/skills/shooting-prep`): cream
background, white cards with thin accent bars, Georgia titles + Calibri body, PASS green /
FAIL red semantics. **The bottom-right 1/3 × 1/3 of every slide (x > 6.67in, y > 3.75in)
stays empty for the talking head** — the build script asserts it. Always render
(`soffice --headless --convert-to pdf`) and look before delivering.
