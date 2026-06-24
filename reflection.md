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
  I used the Antigravity IDE agent (powered by Gemini) and its specialized browser subagents to automate testing the game, taking screenshots, and recording WebP files of each glitch. This allowed me to catalog the behavior of all 8 bugs methodically.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI suggested setting up a dedicated `.project/` configuration directory to keep browser driver profiles and runtime configs out of the root project directory. I verified this by running git status locally and confirming that all temporary test automation assets remained completely ignored.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  The AI initially suggested that I run complex manual terminal commands to configure Chrome driver binaries, but I verified that I could use high-level browser agent calls directly to inspect the page. This saved me from polluting my local environment with manual driver installations.

**Example 2:**

> **What the AI suggested**: Initially, when reproducing the "Type Juggling" bug, the AI and my manual plan assumed testing a guess of 5 against a secret of 50 would expose the bug.
> **Why it was misleading**: The AI failed to account for Python's lexicographical string sorting. Because '5' is evaluated as smaller than '50' alphabetically, the buggy code accidentally returned the correct "Too Low" hint, masking the bug.
> **How I verified it**: I wrote an automated pytest-bdd test for guess 5, and the test unexpectedly passed. I collaborated with the AI to understand the string logic, then changed the test to guess 6 against 50 (since '6' > '50' alphabetically). The test correctly failed, exposing the bug.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

**Bug 2 (Type Juggling)**: I verified this fix using Test-Driven Verification. I created a pytest-bdd scenario (type_juggling.feature) that asserted a guess of 6 against a secret of 50 should return "Too Low". I marked it with @pytest.mark.xfail (Red phase). Once I removed the string casting in app.py, I removed the xfail marker and ran uv run pytest, confirming the test passed (Green phase).

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
