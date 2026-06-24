from pytest_bdd import given, parsers, scenario, then, when


@scenario("../features/hint_messages.feature", "Correct guess results in a Win")
def test_correct_guess_results_in_a_win():
    pass


@scenario("../features/hint_messages.feature", "Guess is too high")
def test_guess_is_too_high():
    pass


@scenario("../features/hint_messages.feature", "Guess is too low")
def test_guess_is_too_low():
    pass


@given(parsers.parse("the secret number is {secret_num:d}"))
def set_secret_number(app_test, secret_num):
    app_test.session_state.secret = secret_num
    app_test.run()


@when(parsers.parse("a player guesses {guess_num:d}"))
def make_guess(app_test, guess_num):
    guess_input = app_test.text_input(key="guess_input_Normal")
    guess_input.input(str(guess_num))

    # Click Submit button
    submit_button = app_test.button[0]
    submit_button.click().run()


@then(parsers.parse('the outcome should be "{expected_outcome}"'))
def verify_outcome(app_test, expected_outcome):
    status_map = {"Win": "won", "Too High": "playing", "Too Low": "playing"}
    assert app_test.session_state.status == status_map[expected_outcome]


@then(parsers.parse('the hint message should be "{expected_message}"'))
def verify_message(app_test, expected_message):
    warning_element = app_test.warning[0]
    actual_message = f"{warning_element.icon or ''} {warning_element.value}".strip()
    assert expected_message == actual_message
