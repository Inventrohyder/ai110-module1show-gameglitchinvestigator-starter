# Workspace Agent Rules

## 1. Stack & Commit Philosophy

- **Latest Dependency Version**: Always use the latest secure and stable dependency/tool versions (e.g. checkout `@v7`, updated linters).
- **Dependency Isolation**: Install development or testing tools (like `pytest`) in dev dependency groups rather than production dependencies.
- **Progressive Documentation**: Fill out reflection documents and tasks progressively at the layer they become relevant, rather than ahead of time.
- **Proper Stack Layering**: Keep PR scopes clean and sequential. Do not preemptively reference ADRs, files, or refactorings that belong to future stack layers.

## 2. Testing Principles

- **E2E Priority**: Prefer real end-to-end tests (e.g. using Streamlit `AppTest` to interact with actual widgets) rather than unit tests or mock-based/fake-state fixtures.
- **Assertion Isolation**: Separate assertions into individual test functions (one assert per test function) to prevent a failure from masking subsequent validation results.
- **No Control Flow or Iterations**: Test functions (including BDD step definitions and unit tests) must not use control flow logic (such as `if`, `else`, `try/except`, `switch`) or loops/iterations (such as `for` loops, list comprehensions, or generator expressions) that alter assertion behavior or verify multiple conditions.
- **Static test marking**: Do not use dynamic or conditional check-marks to bypass test execution based on current logic state. Statically mark tests as expected to fail (`@pytest.mark.xfail`) at the layer where they are buggy, and remove the marker at the layer where the fix is implemented.
