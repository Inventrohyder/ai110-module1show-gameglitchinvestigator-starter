# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
| --------- | ----------- | ----------------- | ------------ | -------------- |
|           |             |                   |              |                |
|           |             |                   |              |                |
|           |             |                   |              |                |

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

<!-- Describe what you asked each model to do -->

|                          | Model A | Model B |
| ------------------------ | ------- | ------- |
| **Model name**           |         |         |
| **Response summary**     |         |         |
| **More Pythonic?**       |         |         |
| **Clearer explanation?** |         |         |

**Which did you prefer and why?**

<!-- Your conclusion -->
