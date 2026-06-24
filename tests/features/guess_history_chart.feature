Feature: Guess History Chart Data Tracking
  As a player
  I want my guess distances to be tracked sequentially
  So that I can visualize my accuracy trends over multiple attempts

  Scenario: Submitting a valid guess logs absolute distance from secret
    Given the game difficulty is configured to "Normal"
    And the secret number is set to 50
    When the player submits a guess of 65
    Then the distance tracking array should contain 15