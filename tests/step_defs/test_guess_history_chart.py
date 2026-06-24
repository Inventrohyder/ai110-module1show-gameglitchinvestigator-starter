from pytest_bdd import given, parsers, scenario, then, when


@scenario(
    "../features/guess_history_chart.feature",
    "Submitting a valid guess logs absolute distance from secret",
)
def test_submitting_valid_guess_logs_absolute_distance():
    pass


@given(parsers.parse('the game difficulty is configured to "{difficulty}"'))
def set_difficulty(app_test, difficulty):
    app_test.sidebar.selectbox[0].select(difficulty).run()


@given(parsers.parse("the secret number is set to {secret_num:d}"))
def set_secret_number(app_test, secret_num):
    app_test.session_state.secret = secret_num
    app_test.run()


@when(parsers.parse("the player submits a guess of {guess_num:d}"))
def make_guess(app_test, guess_num):
    guess_input = app_test.text_input(key="guess_input_Normal")
    guess_input.input(str(guess_num))

    # Click Submit Guess button
    submit_button = app_test.button[0]
    submit_button.click().run()


@then(parsers.parse("the distance tracking array should contain {expected_distance:d}"))
def verify_distance_history_element(app_test, expected_distance):
    # Strict rule compliance: no loops or iterations. Direct array index inspection.
    assert app_test.session_state.distances[0] == expected_distance
