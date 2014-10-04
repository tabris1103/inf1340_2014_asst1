#!/usr/bin/env python3
""" Module to test exercise3.py """

__author__ = 'Kyungho Jung & Christine Oh'
__status__ = "Completed"

# imports one per line

import pytest
from exercise3 import decide_rps

# Test procedures to check whether the decide_rps function outputs
# correct game results when player1 and player2 inputs are valid.
def test_decide_rps():
    """
    Inputs that are valid (have the correct format and length)
    """

    # Case - Player 1 Wins
    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("Scissors", "Paper") == 1

    # Case - Player 2 Wins
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Paper", "Scissors") == 2

    # Case - Ties
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Paper", "Paper") == 0


# Test procedures to check whether the decide_rps function correctly
# raises an exception (error message) when player1 and player2 inputs are invalid.
def test_inputs():
    """
    Inputs that are incorrect format
    """
    with pytest.raises(TypeError):

        # One of the input is not string value
        decide_rps(1, "Rock")

    with pytest.raises(TypeError):
        decide_rps("Rock", 1)

    with pytest.raises(TypeError):
        #Float and integer passed
        decide_rps(2.231,1)

    with pytest.raises(TypeError):
            decide_rps("Rock", False)

    with pytest.raises(TypeError):
        # Boolean Value Passed
        decide_rps(True, "Rock")

    # One of the player input is wrong string value
    with pytest.raises(ValueError):
        decide_rps("Rock", "P")
    with pytest.raises(ValueError):
        decide_rps("R", "Paper")

    # One of the player input's first character is not capitalized properly
    with pytest.raises(ValueError):
        decide_rps("rock", "Paper")
    with pytest.raises(ValueError):
        decide_rps("Rock", "paper")

    # One of the player input is numeric string value
    with pytest.raises(ValueError):
        decide_rps("1", "2")
    with pytest.raises(ValueError):
        decide_rps("Rock", "1")

# other tests

