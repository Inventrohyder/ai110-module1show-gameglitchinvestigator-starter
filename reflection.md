# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game loaded with a title, difficulty settings, and a developer debug info panel. However, the hints directed me in the opposite direction of the secret number, the score fluctuated on incorrect guesses, and even attempts caused comparison logic errors.
- List at least two concrete bugs you noticed at the start
  1. The hints were inverted (e.g. telling me to go higher when my guess was too high).
  2. Type juggling on even attempts caused incorrect comparisons and hints.

### Bug Reproduction Log

Document at least 3 bugs you found. Add rows as needed.

| Input                                                   | Expected Behavior                                                                          | Actual Behavior                                                                                                    | Console Output / Error                                                                                                   | GitHub Issue                                                                                     | Recording                                                              |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| Guess `60` when secret is `50`                          | Display warning hint "📈 Go LOWER!" (or equivalent)                                        | Displays warning hint "📈 Go HIGHER!"                                                                              | None                                                                                                                     | [#1](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/issues/1) | [bug1_inverted_hints.webp](docs/recordings/bug1_inverted_hints.webp)   |
| Guess `9` on Attempt 2 (secret is `50`)                 | Hint correctly indicates if guess is too high/low using integer comparison                 | Secret is cast to string, string comparison `"9" > "50"` evaluates to True, and hint incorrectly says "Go HIGHER!" | `TypeError: '>' not supported between instances of 'int' and 'str'` (internally caught and juggled to string comparison) | [#2](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/issues/2) | [bug2_type_juggling.webp](docs/recordings/bug2_type_juggling.webp)     |
| Select "Hard" difficulty                                | Sidebar shows a larger range (e.g. 1 to 200)                                               | Sidebar displays "Range: 1 to 50"                                                                                  | None                                                                                                                     | [#3](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/issues/3) | [bug3_hard_range.webp](docs/recordings/bug3_hard_range.webp)           |
| Make an incorrect guess                                 | Score remains unchanged until winning or losing                                            | Score decreases/increases mid-game                                                                                 | None                                                                                                                     | [#4](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/issues/4) | [bug4_score_incorrect.webp](docs/recordings/bug4_score_incorrect.webp) |
| Select "Easy" difficulty (range 1-20)                   | Info banner says "Guess a number between 1 and 20"                                         | Info banner says "Guess a number between 1 and 100"                                                                | None                                                                                                                     | [#5](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/issues/5) | [bug5_static_banner.webp](docs/recordings/bug5_static_banner.webp)     |
| Guess correctly on Attempt 1                            | Award 90 points (100 - 10 \* 1)                                                            | Awards 80 points or less (incorrect attempt off-by-one logic)                                                      | None                                                                                                                     | [#6](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/issues/6) | [bug6_score_formula.webp](docs/recordings/bug6_score_formula.webp)     |
| Click "New Game 🔁" after winning                       | Reset score to 0, clear guess history, and set status to "playing"                         | Score, history, and status ("won") are retained, blocking the user from playing again                              | None                                                                                                                     | [#7](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/issues/7) | [bug7_new_game_reset.webp](docs/recordings/bug7_new_game_reset.webp)   |
| Run `pytest` with existing tests                        | Tests pass when checking outcome                                                           | Tests fail because `check_guess` returns a tuple but tests assert on a single string                               | `AssertionError: assert ('Win', '🎉 Correct!') == 'Win'` (or `NotImplementedError`)                                      | [#8](https://github.com/Inventrohyder/ai110-module1show-gameglitchinvestigator-starter/issues/8) | N/A                                                                    |
| Click "Submit Guess 🚀" with empty or non-numeric input | Validation error is shown, attempts counter does not increment, and history is not updated | Attempts counter increments (wasting an attempt) and invalid input (e.g. empty string) is appended to history      | None                                                                                                                     | N/A                                                                                              | N/A                                                                    |

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used the Antigravity IDE agent (powered by Gemini) and its specialized browser subagents to automate testing the game and capturing recordings of each glitch. Later, I used the same platform to coordinate my implementation planning, test generation, and refactoring tasks.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI suggested using Streamlit's `AppTest` framework for simulating the UI instead of manually mocking internal dictionaries in tests. It also correctly suggested setting up a dedicated `.project/` directory to isolate local configuration assets. I verified both suggestions by successfully running automated tests with `pytest` and checking that `git status` remained clean.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  The AI initially suggested a Git branching strategy using a separate `develop` branch and writing temporary branch updates to `CHANGELOG.md`. I corrected it to use trunk-based development on `main` and keep the changelog relative to the base branch. It also suggested manual setup of browser driver binaries, which I replaced with clean high-level test run calls.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decided a bug was fixed when the corresponding pytest-bdd Gherkin scenario passed, the Streamlit AppTest simulation test succeeded without errors, and manual visual validation in the browser confirmed correct behavior.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran `uv run pytest` to execute the Gherkin feature tests. It showed me that the initial `check_guess` implementation returned a tuple but existing tests asserted on a string outcome, causing type mismatches.
- Did AI help you design or understand any tests? How?
  Yes, the AI helped scaffold the pytest-bdd step definitions and the Streamlit AppTest simulation structure, which allowed me to run automated UI tests without starting a full browser on every code change.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit is like a flipbook that redraws the entire page from top to bottom every time you click a button or type in an input box. Because it runs the whole script again on every interaction, any normal variables would get reset to their starting values. Session state is like a notepad that Streamlit keeps on the side; it lets us save numbers, scores, and status across these reruns so the app remembers what happened in previous steps.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    I want to reuse the Graphite stacked PR workflow and on-demand documentation updates. Addressing PR feedback and logging AI interactions immediately inside the correct branch layer keeps the development stack extremely clean and organized.
- What is one thing you would do differently next time you work with AI on a coding task?
  Next time, I will configure linter rules and CI pipelines before starting any feature or bug fix branch. This prevents formatting/style issues from cluttering downstream commits and avoids having to fix checks later in the stack.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project showed me that AI-generated code is highly effective for bootstrapping and automation, but requires structured guardrails and careful human review to ensure architectural alignment. Treat the AI as an active pair programmer rather than a black-box generator.
