import pytest
from streamlit.testing.v1 import AppTest


def test_app_title():
    at = AppTest.from_file("app.py")
    at.run()
    assert at.title[0].value == "🎮 Game Glitch Investigator"


@pytest.mark.xfail(
    reason="AppTest simulation fails because hints are inverted and secret type is juggled"
)
def test_app_inverted_hints_simulation():
    at = AppTest.from_file("app.py")
    at.run()

    # Retrieve the secret number from session state/debug info
    secret = at.session_state.secret

    # Enter a guess that is larger than the secret
    guess_val = secret + 5
    guess_input = at.text_input(key="guess_input_Normal")
    guess_input.input(str(guess_val))

    # Submit guess
    submit_button = (
        at.button(key="submit") if "submit" in at.session_state else at.button[0]
    )
    submit_button.click().run()

    # Assert that the warning message advises the player to go LOWER
    # Currently it will say "Go HIGHER!" because hints are inverted, so this assertion will fail.
    warning_messages = [w.value for w in at.warning]
    assert any("Go LOWER!" in msg for msg in warning_messages)
