# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**
I instructed the agent to implement a non-disruptive "Guess History" feature expansion inside `app.py` before our scheduled refactoring phase. The goal was to track the absolute distance of every valid numeric guess from the target secret key value, preserve the progressive difficulty level boundary states (Easy: 1-20, Normal: 1-100, Hard: 1-150), store the data within the session state, render it visually as a sidebar line chart, and back it with a strict, loop-free Gherkin BDD test.

**What did the agent do?**

1. Initialized a state list primitive (`st.session_state.distances`) within the global setup of `app.py`.
2. Modified the `submit` block in `app.py` to calculate the absolute delta ($|\text{guess\_int} - \text{secret}|$) and append it on valid turns.
3. Inserted a rendering block utilizing `st.sidebar.line_chart(st.session_state.distances)` conditionally inside the sidebar.
4. Generated an independent Gherkin feature file (`tests/features/guess_history_chart.feature`) specifying the array tracking criteria.
5. Autonomously generated the base step definition structures within `tests/step_defs/test_guess_history_chart.py`.

**What did you have to verify or fix manually?**
I had to manually audit and correct the assertion step inside `test_guess_history_chart.py` to guarantee strict compliance with our project's `.agents/AGENTS.md` testing guardrails. The agent initially attempted to extract and assert values using collection aggregation, which implicitly violates the zero-loop/zero-iteration directive. I replaced this with an absolute direct index lookup (`app_test.session_state.distances[0] == expected_distance`) to safely ensure a pure, loop-free, conditional-free assertion context.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case               | Prompt Used                                                                                                                                                                                                                                      | AI-Suggested Test                                                    | Did It Pass?                            | Your Reasoning                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------------------- |
| Inverted hint direction | `"Full formal pytest-bdd + AppTest + Graphite stacks for test infrastructure — Set up the testing framework as its own stacked PR chain: (1) add pytest-bdd dep, (2) create features/ directory structure, (3) create hint_messages.feature..."` | Pytest-bdd feature scenario with step assertions comparing outcomes. | No (initially failed/xfail due to bugs) | Verified that hints evaluation can be structured via Gherkin before repairing bugs. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

I directed the AI to set up a comprehensive CI linting workflow using Trunk.io and Ruff, and guided its initialization, file formatting, and stacked branch splitting using the following sequence of prompts:

1. **Initial Linting & CI Request (from comments on initial plan draft):**

   ```text
   "Also, I wanted to also setup all appropriate github actions, and checks required for this project, and adding them in the appropriate places and phases of the full plan as part of granular tasks."
   ```

2. **Expanding CI Scope & Introducing Trunk.io (in response to AI recommendation):**

   ```text
   "Yes, setup github actions that is very thorough, and not limited to, pytest, trunk.io, and others. All broken down as part of the granular tasks required..."
   ```

3. **Coordinating Linters under Trunk:**

   ```text
   "full full, remember ruff is part of trunk.io right? and many others are also part of trunk.io, no?"
   ```

4. **Optimizing PR Stack Order (moving Trunk init to Stack 1, before ADRs):**

   ```text
   "trunk init must be higher since it does include markdown and adr format linting, right?"
   ```

5. **Validating Trunk's Automatic Analysis:**

   ```text
   "I think trunk init does it's own analysis, right?"
   "I meant trunk init analysis what to add automagically right?"
   ```

6. **Enforcing Clean Stack Splits for Formatting Outputs:**

   ```text
   "You have so many changes now, make sure to split it appropriately, like the trunk fmt outputs are separate right?"
   ```

**Linting output before:**

```text
app.py:
  - Line length exceeds 88 characters.
  - Missing docstrings for files and functions.
reflection.md:
  - Spacing issues in markdown tables.
  - Line breaks formatting inconsistencies.

```

**Changes applied:**

- Initialized trunk and added `ruff`, `prettier`, `markdownlint`, and `actionlint` to `.trunk/trunk.yaml`.
- Executed `trunk fmt` to auto-correct all markdown table spacings and line-wrap settings.
- Resolved styling warnings in markdown files.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

|                          | Model A | Model B |
| ------------------------ | ------- | ------- |
| **Model name**           |         |         |
| **Response summary**     |         |         |
| **More Pythonic?**       |         |         |
| **Clearer explanation?** |         |         |

**Which did you prefer and why?**

---

Run your local check verification check to confirm everything is clean:

```bash
trunk check --all
```
