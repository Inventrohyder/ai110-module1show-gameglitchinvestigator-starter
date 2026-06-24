Feature: Difficulty Ranges
  As a player
  I want the game difficulties to be progressively harder
  So that the game provides an appropriate challenge at each level

  Scenario Outline: Difficulty sets the correct range
    Given the game difficulty is configured to "<difficulty>"
    Then the range displayed should be "<expected_range>"

    Examples:
      | difficulty | expected_range   |
      | Easy       | Range: 1 to 20   |
      | Normal     | Range: 1 to 100  |
      | Hard       | Range: 1 to 150  |
      