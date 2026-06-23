# Use pytest-bdd for Gherkin-Based Behavioral Testing

- Status: accepted
- Deciders: Antigravity, USER
- Date: 2026-06-23

## Context and Problem Statement

To prevent regressions and systematically fix the game glitches in a structured manner, we need a testing framework that:

- Integrates with standard Python test runners (`pytest`).
- Supports human-readable feature descriptions (Gherkin syntax) to write test specifications easily.
- Promotes behavioral-driven development (BDD) by checking features in terms of Given-When-Then scenarios.

We need to add BDD testing infrastructure to the project.

## Decision Drivers

- Human-readable specifications matching business requirements.
- Integration with standard `pytest` framework and CI pipelines.
- Capability to isolate and reproduce glitches as failed test scenarios prior to fixing them.

## Considered Options

1. **Vanilla unittest/pytest**: standard code unit tests. They work well but do not provide high-level, human-readable Gherkin scenarios.
2. **pytest-bdd**: BDD library for pytest that parses Gherkin feature files and runs step definitions written in normal Python.
3. **Behave**: standalone BDD tool, but does not integrate as seamlessly with existing pytest plugins or custom execution options.

## Decision Outcome

Chosen option: **pytest-bdd** (Option 2), because it enables writing Gherkin feature files that describe high-level behaviors while running under our existing standard `pytest` runner, allowing seamless integration with our CI workflows.

### Positive Consequences

- Separate, clean `.feature` files describing user flows in plain language.
- Reusable steps in step definitions.
- Easy alignment with the visual and game rules specified in the instructions.

### Negative Consequences

- Requires maintaining Gherkin scenarios alongside Python step definitions.
