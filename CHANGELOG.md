# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial scaffolding for project documentation.
- Migrated project setup to uv.
- Integrated Trunk.io linter framework (ruff, markdownlint, prettier, actionlint).
- Configured CI workflows on GitHub Actions for pytest and trunk check.
- Recorded and documented all 8 core game glitches with clean screen recordings.
- Updated `reflection.md` to link all identified glitches to their corresponding GitHub issues and recording files.
- Configured pytest-bdd Gherkin-based behavioral testing dependency.

### Changed

### Fixed

- Swapped inverted hint message emojis and text inside check_guess to guide players in the correct direction (bug [#1](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/issues/1)).
- Removed erroneous string type-casting on even attempts to prevent incorrect alphabetical comparisons against numeric guesses (bug [#2](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/issues/2)).

### Removed

### Security
