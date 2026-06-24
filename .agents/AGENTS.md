# Workspace Agent Rules

These rules govern the behavior of AI coding assistants (including Antigravity, Claude, and Copilot) in this repository. All agents MUST follow these instructions.

## 1. Stacked Branch & CI Trigger Rules

- **PR Workflow Triggers**: Always verify that GitHub Actions workflows (`.github/workflows/test.yml`, `.github/workflows/trunk-check.yml`, etc.) are triggered on the `pull_request` event _without_ restricting them to the `main` branch. In a Graphite stacked PR environment, PRs target the branch directly below them, not `main`. Removing branch restrictions ensures that CI status checks execute for every PR in the stack.

## 2. Testing & Mocking Rules

- **No Mocks/Fakes in BDD step definitions**: When implementing Gherkin behavioral scenarios (`pytest-bdd`), do NOT use mocked session state dictionaries or call isolated Python functions (e.g. `check_guess`) directly if the goal is to verify the software experience. You MUST test the actual Streamlit application end-to-end using the official Streamlit `AppTest` simulation API (loading `app.py`, inputting values into widgets, clicking buttons, and asserting on rendered outputs like `warning`, `error`, `success`, and session state).

## 3. Workflow Order Rules

- **Bug Repair first, Refactoring second**: Do not attempt to refactor the core codebase (such as extracting core game functions to `logic_utils.py`) before all bugs have been identified, Gherkin scenarios written (marked as xfail), and the bugs repaired and verified. Write code fixes first (Red-Green-Refactor order).

## 4. Asset Integrity Rules

- **Validate browser recordings**: When generating recordings of bugs or features using browser subagents (WebP videos), always verify the file sizes and playability of the files. Ensure that:
  1. No duplicate timestamped version is committed alongside the clean target version.
  2. No recording is truncated or corrupted (e.g., 11KB empty files) due to a cancelled or interrupted subagent session.

## 5. Documentation & Changelog Rules

- **Strict Changelog Scope**: `CHANGELOG.md` entries must only reflect changes relative to the base branch (`main`), not internal corrections or iterations made within local branches of the same PR stack.

## 6. Stack & Commit Philosophy

- **Latest Dependency Version**: Always use the latest secure and stable dependency/tool versions (e.g. checkout `@v7`, updated linters).
- **Dependency Isolation**: Install development or testing tools (like `pytest`) in dev dependency groups rather than production dependencies.
- **Progressive Documentation**: Fill out reflection documents and tasks progressively at the layer they become relevant, rather than ahead of time.
- **Proper Stack Layering**: Keep PR scopes clean and sequential. Do not preemptively reference ADRs, files, or refactorings that belong to future stack layers.

## 7. Testing Principles

- **E2E Priority**: Prefer real end-to-end tests (e.g. using Streamlit `AppTest` to interact with actual widgets) rather than unit tests or mock-based/fake-state fixtures.
- **Assertion Isolation**: Separate assertions into individual test functions (one assert per test function) to prevent a failure from masking subsequent validation results.
- **No Control Flow or Iterations**: Test functions (including BDD step definitions and unit tests) must not use control flow logic (such as `if`, `else`, `try/except`, `switch`) or loops/iterations (such as `for` loops, list comprehensions, or generator expressions) that alter assertion behavior or verify multiple conditions.
- **Static test marking**: Do not use dynamic or conditional check-marks to bypass test execution based on current logic state. Statically mark tests as expected to fail (`@pytest.mark.xfail`) at the layer where they are buggy, and remove the marker at the layer where the fix is implemented.
