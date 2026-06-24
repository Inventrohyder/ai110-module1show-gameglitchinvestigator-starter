---
name: pr-feedback-guardrails
description: Workspace guardrails to prevent common stacked PR, mocking, workflow order, and asset corruption bugs.
---

# PR Feedback Guardrails Skill

Use this skill when initializing the environment, working on stacked PR branches, writing integration tests, and validating assets before commits.

## Stacked PR Configuration

In a stacked PR environment where branches are stacked sequentially (e.g. via Graphite), pull request workflows MUST NOT be restricted to run only when targeting `main`. Configure `.github/workflows/*.yml` with the following trigger structure to ensure that check runs trigger for every branch in the stack:

```yaml
on:
  push:
    branches: [main]
  pull_request:
```

## Streamlit e2e Testing Rules

Do not use mock state tables or dictionaries to verify app behavior. Use Streamlit's official `AppTest` API to simulate user interactions directly:

1. Load the app: `at = AppTest.from_file("app.py")`
2. Run initial load: `at.run()`
3. Set secret values in state if needed: `at.session_state.secret = X`
4. Interact with widgets:
   - Type input: `at.text_input(key="guess_input_Normal").input("50")`
   - Click submit button: `at.button[0].click().run()`
5. Assert on outcomes:
   - Success blocks: `any("You won!" in msg for msg in [s.value for s in at.success])`
   - Warning hints: `any("Go LOWER!" in msg for msg in [w.value for w in at.warning])`

## Asset Validation

Always verify generated media files before staging:

- Ensure no timestamped duplicates (e.g., `bug_hard_range_*.webp`) are committed.
- Verify file sizes to ensure they are complete recordings (corrupt/truncated recordings are typically ~11KB).
