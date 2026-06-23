Feature: Hint Direction and Guess Checking
  Players should receive accurate hints telling them whether to go HIGHER or LOWER
  based on their guesses compared to the secret number.

  Scenario: Correct guess results in a Win
    Given the secret number is 50
    When a player guesses 50
    Then the outcome should be "Win"
    And the hint message should be "🎉 Correct!"

  Scenario: Guess is too high
    Given the secret number is 50
    When a player guesses 60
    Then the outcome should be "Too High"
    And the hint message should be "📉 Go LOWER!"

  Scenario: Guess is too low
    Given the secret number is 50
    When a player guesses 40
    Then the outcome should be "Too Low"
    And the hint message should be "📈 Go HIGHER!"
