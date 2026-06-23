# 🎮 Game Glitch Investigator: The Impossible Guesser

[![test](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/actions/workflows/test.yml/badge.svg)](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/actions/workflows/test.yml)
[![trunk-check](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/actions/workflows/trunk-check.yml/badge.svg)](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/actions/workflows/trunk-check.yml)

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `uv sync`
2. Run the broken app: `uv run streamlit run app.py`

## 🧪 Testing

This project uses `pytest` and `pytest-bdd` to run behavioral tests defined in Gherkin syntax, using Streamlit `AppTest` for automated end-to-end UI simulations.

To run the test suite:

```sh
uv run pytest
```

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot** _(optional)_: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```text
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

## 🎨 Linting & Formatting

We use [Trunk.io](https://trunk.io/) to enforce consistent code quality, formatting, and linting rules.

### Running Linters Locally

- Format all files:
  ```sh
  trunk fmt
  ```
- Lint check modified files:
  ```sh
  trunk check
  ```
- Run checks on the entire repository:
  ```sh
  trunk check --all
  ```

### Installing Git Hooks

To automatically format on commit and run lint checks before pushing:

```sh
trunk git-hooks install
```
