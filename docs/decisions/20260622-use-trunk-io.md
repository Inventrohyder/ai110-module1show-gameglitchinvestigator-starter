# Use Trunk.io for Linting and Code Quality

- Status: accepted
- Deciders: Antigravity, USER
- Date: 2026-06-22

## Context and Problem Statement

To maintain code quality, formatting consistency, and catch early bugs, we need a unified linting and formatting workflow. Running multiple linters (Ruff, Prettier, Markdownlint, Actionlint) manually or configuring them separately in CI can lead to configuration drift and developer overhead.

## Decision Drivers

- Consistent formatting across Python, Markdown, and configuration files.
- Single tool interface for developers to run all checks locally.
- Out-of-the-box integration with CI.
- Fast, incremental checking of modified files only.

## Considered Options

1. **Manual linter setup**: Individual configurations for Ruff, Prettier, Markdownlint, and Actionlint.
2. **Pre-commit hooks framework**: Configuring pre-commit with individual hooks.
3. **Trunk.io**: Unified CLI checker and formatter toolchain.

## Decision Outcome

Chosen option: **Trunk.io** (Option 3), because it manages linter toolchains seamlessly, provides version pinning, allows single-command local formatting/checking (`trunk fmt` / `trunk check`), and has native support for the desired linters.

In addition, we configured automated git hooks (`trunk-check-pre-push` and `trunk-fmt-pre-commit`) via Trunk CLI actions to format code on commit and run lint checks before push.

### Positive Consequences

- Simple configuration via `.trunk/trunk.yaml`.
- Automatic version pinning of linters and formatters (using latest compatible stable versions: `ruff@0.0.290`, `markdownlint@0.41.0`, `prettier@3.8.4`, `actionlint@1.6.9` to ensure compatibility with the pinned Node.js toolchain).
- High speed due to incremental caching.
- Developers are guarded from committing unformatted code or pushing lint failures locally.

### Negative Consequences

- Developers must install the `trunk` CLI tool.
