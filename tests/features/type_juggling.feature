Feature: Type Juggling on Even Attempts
  As a player
  I want my guesses to be compared numerically against the secret number
  So that alphabetical sorting does not lead to incorrect hints

  Scenario: Incorrect hint due to type juggling on first guess
    Given the game difficulty is configured to "Normal"
    And the secret number is set to 50
    When the player submits a guess of 6
    Then the warning hint should be "📈 Go HIGHER!"