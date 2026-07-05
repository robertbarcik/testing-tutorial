# Testing Tutorial: Testing LLM Applications

A hands-on progression through testing LLM applications, from manual spot-checks to automated
pipelines and security testing. Each notebook builds on the previous one.

## The testing ladder

| Notebook | What it covers |
|----------|-----------------|
| `00_Basic_Testing.md` | Manual testing without tools: probing an LLM by hand in a chat interface for hallucinations, consistency, and edge cases |
| `01_llm_testing_manual_to_automated.ipynb` | Turning manual checks into automated pytest tests: assertions, parameterized tests, Pydantic validation of structured outputs |
| `02_testing_adk_agents.ipynb` | Testing agents (not just single LLM calls) built with Google's ADK: verifying tool selection, tool parameters, and multi-step reasoning |
| `03_llm_as_judge_evaluation.ipynb` | LLM-as-judge for subjective qualities (helpfulness, tone, ethics) that plain assertions cannot check, using a banking agent as the example |
| `04_evaluation_pipeline.ipynb` | Combining assertions, tool-call heuristics, and LLM judges into a single reusable `AgentEvaluator` pipeline with reports and dashboards |
| `05_llm_security_testing.ipynb` | Security testing basics: system prompt extraction, direct prompt injection, and comparing how different models resist the same attacks |
| `06_advanced_llm_security.ipynb` | Advanced attacks: indirect injection via documents and data, data poisoning, and bypassing an LLM guardrail |

## How to run

**Colab is recommended** - open any notebook in Google Colab, add your API key(s) to Colab
Secrets (the key icon in the left sidebar), and run cells top to bottom.

**To run locally instead:**

1. Python 3.10 or newer.
2. `pip install -r requirements.txt`
3. Set the API keys you need as environment variables before launching Jupyter (the notebooks
   now read from the environment automatically, no manual entry required):
   - `OPENAI_API_KEY` - needed for notebooks 01-04
   - `OPENROUTER_API_KEY` - needed for notebooks 05-06
4. Launch Jupyter and run each notebook top to bottom.

If neither Colab Secrets nor an environment variable is found, the auth cell falls back to an
interactive `getpass()` prompt.

## Cost

All notebooks use small, cheap models (`gpt-5-nano` for 01-04, small open-source models via
OpenRouter for 05-06). Running the entire tutorial end to end costs well under two dollars.

## Companion course

This repository is the hands-on companion to the "EU AI Act for Developers" Udemy course,
supporting its Article 15 modules on accuracy, robustness, and cybersecurity of high-risk AI
systems.
