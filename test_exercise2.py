#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest
from exercise2 import checksum


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    assert checksum("123412341234") is False


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)
    with pytest.raises(TypeError):
        checksum(786936224306)
    with pytest.raises(TypeError):
        checksum(False)
    with pytest.raises(TypeError):
        checksum("12341234" + 1234)

    # Raise ValueError when the length of the input is not equal to 12
    with pytest.raises(ValueError):
        checksum("1")
    with pytest.raises(ValueError):
        checksum("1234567890")
    with pytest.raises(ValueError):
        checksum("1234123412341")

    # Raise ValueError if one or more of the input values are not numeric
    with pytest.raises(ValueError):
        checksum("123s56789011")
    with pytest.raises(ValueError):
        checksum("abcdefghijkl")
    with pytest.raises(ValueError):
        checksum("123*45@67890")

    # Raise ValueError if negative input was entered
    with pytest.raises(ValueError):
        checksum("-212341231")

