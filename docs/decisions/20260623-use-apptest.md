# Use Streamlit AppTest for UI Simulation Testing

- Status: accepted
- Deciders: Antigravity, USER
- Date: 2026-06-23

## Context and Problem Statement

Streamlit apps run inside a browser context, which makes traditional unit testing of page layouts, state updates, and widgets challenging without full browser automation frameworks like Selenium or Playwright.

We need a lightweight, fast, and programmatic tool to simulate user interactions and state changes in the Streamlit app.

## Decision Drivers

- Speed of test execution (sub-second UI tests).
- Programmatic control over inputs, buttons, and session state.
- No need to spin up a full browser subagent or selenium grid in CI pipelines.

## Considered Options

1. **Selenium/Playwright**: Full browser testing. Very thorough but slow, heavy, complex to configure in CI, and prone to flakiness.
2. **Streamlit AppTest**: Official testing API added in Streamlit `v1.28.0+`. It executes the app script in a mock environment and provides inspection APIs for widgets, status indicators, and session state.

## Decision Outcome

Chosen option: **Streamlit AppTest** (Option 2), because it allows us to programmatically simulate user guesses, clicks on "New Game", and settings updates without the overhead of browser execution, enabling fast, robust validation of UI states in our test runner and CI pipelines.

### Positive Consequences

- Sub-second UI/Widget test execution.
- Direct access to widgets by key and session state fields.
- Easily asserts warning/error/success boxes and🎈balloons.

### Negative Consequences

- Does not test visual formatting (CSS, pixel placement) or browser-specific rendering bugs.
