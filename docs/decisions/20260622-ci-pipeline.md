# CI Pipeline with GitHub Actions

- Status: accepted
- Deciders: Antigravity, USER
- Date: 2026-06-22

## Context and Problem Statement

To prevent broken code and linting failures from being merged into the `main` branch, we need automated checks that execute on every commit and pull request.

## Decision Drivers

- Fast feedback loops for pull requests.
- Enforcement of code cleanliness via Trunk.io check.
- Verification of test suite correctness via pytest and uv.
- Simple maintenance of CI scripts.

## Considered Options

1. **Local verification only**: Developers run formatters/tests manually before pushing.
2. **GitHub Actions**: Native GitHub CI/CD environment with simple configuration yaml files.
3. **Trunk Flakiness / CI SaaS**: Dedicated third-party CI service.

## Decision Outcome

Chosen option: **GitHub Actions** (Option 2), because it is free for public repositories, integrates natively with GitHub PR status checks, and has pre-built actions for both `uv` (`astral-sh/setup-uv`) and Trunk (`trunk-io/trunk-action`).

### Positive Consequences

- Merges are blocked on `main` if tests or linter checks fail.
- Consistent and clean environment for test execution (eliminates "works on my machine" issues).

### Negative Consequences

- GitHub Actions syntax and configuration yaml files must be maintained.
