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

# Test valid inputs


def test_valid_inputs():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("R", "P") == 2
    assert decide_rps("S", "S") == 0
    assert decide_rps("R", "S") == 1

# Test invalid inputs


def test_invalid_inputs():
    """
    Inputs that are incorrect format
    """
    with pytest.raises(TypeError):
        decide_rps("1", "2")
    with pytest.raises(ValueError):
        decide_rps("Rock", "Paper")


# other tests

