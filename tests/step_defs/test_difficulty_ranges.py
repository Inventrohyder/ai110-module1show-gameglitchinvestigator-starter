from pytest_bdd import given, parsers, scenario, then


@scenario("../features/difficulty_range.feature", "Difficulty sets the correct range")
def test_difficulty_sets_correct_range():
    pass


@given(parsers.parse('the game difficulty is configured to "{difficulty}"'))
def set_difficulty(app_test, difficulty):
    # Direct widget interaction without loops
    app_test.sidebar.selectbox[0].select(difficulty).run()


@then(parsers.parse('the range displayed should be "{expected_range_text}"'))
def verify_range_displayed(app_test, expected_range_text):
    # Direct index access to completely eliminate the list comprehension iteration
    assert app_test.sidebar.caption[0].value == expected_range_text
