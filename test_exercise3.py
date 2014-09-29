#!/usr/bin/env python3
""" Module to test exercise3.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

import pytest
from exercise3 import decide_rps

# Test procedures to check whether decide_rps function correctly or not
# when the valid input parameters have been passed.
def test_decide_rps():
    """
    Inputs that are the correct format and length
    """

    # Case - Player 1 Wins
    assert decide_rps("P", "R") == 1
    assert decide_rps("R", "S") == 1
    assert decide_rps("S", "P") == 1

    # Case - Player 2 Wins
    assert decide_rps("R", "P") == 2
    assert decide_rps("S", "R") == 2
    assert decide_rps("P", "S") == 2

    # Case - Ties
    assert decide_rps("R","R") == 0
    assert decide_rps("S","S") == 0
    assert decide_rps("P","P") == 0

# Test procedures to check whether decide_rps function handles the exception properly or not
# when the invalid inputs (in terms of format or value) have been passed.
def test_inputs():
    """
    Inputs that are incorrect format
    """
    with pytest.raises(TypeError):
        decide_rps(1, "R")
        decide_rps("R", 1)
        decide_rps(2,1)
        decide_rps(P, R)

    with pytest.raises(ValueError):
        decide_rps("Rock", "P")
        decide_rps("R", "Paper")
        decide_rps("1", "2")

# other tests

