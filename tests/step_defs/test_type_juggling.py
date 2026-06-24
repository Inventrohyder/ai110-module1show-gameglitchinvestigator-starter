# import pytest
from pytest_bdd import given, parsers, scenario, then, when
from streamlit.testing.v1 import AppTest

# # Statically mark the scenario as expected failure during the Red phase
# pytestmark = pytest.mark.xfail(
#     reason="Bug 2: Type-juggling on even attempts causes alphabetical comparison"
# )


@scenario(
    "../features/type_juggling.feature",
    "Incorrect hint due to type juggling on first guess",
)
def test_incorrect_hint_due_to_type_juggling_on_first_guess():
    pass


@given(parsers.parse('the game difficulty is configured to "{difficulty}"'))
def set_difficulty(app_test, difficulty):
    at = AppTest.from_file("app.py")
    at.run()
    return at


@given(parsers.parse("the secret number is set to {secret_num:d}"))
def set_secret_number(app_test, secret_num):
    app_test.session_state.secret = secret_num
    app_test.run()


@when(parsers.parse("the player submits a guess of {guess_num:d}"))
def make_guess(app_test, guess_num):
    guess_input = app_test.text_input(key="guess_input_Normal")
    guess_input.input(str(guess_num))

    # Click Submit button
    submit_button = app_test.button[0]
    submit_button.click().run()


@then(parsers.parse('the warning hint should be "{expected_message}"'))
def verify_message(app_test, expected_message):
    warning_element = app_test.warning[0]
    actual_message = f"{warning_element.icon or ''} {warning_element.value}".strip()
    assert expected_message == actual_message
