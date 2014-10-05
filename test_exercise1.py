#!/usr/bin/env python3

""" Module to test exercise1.py """

__author__ = 'Kyungho Jung & Christine Oh'
__status__ = "Completed"

# imports one per line
import pytest
from exercise1 import grade_to_gpa


def test_letter_grade():
    """
    Letter grade inputs
    """
    assert grade_to_gpa("A+") == 4.0
    assert grade_to_gpa("A") == 4.0
    assert grade_to_gpa("A-") == 3.7
    assert grade_to_gpa("B+") == 3.3
    assert grade_to_gpa("B") == 3.0
    assert grade_to_gpa("B-") == 2.7
    assert grade_to_gpa("FZ") == 0.0

    # Test for invalid letter grade input
    with pytest.raises(ValueError):
        grade_to_gpa("Q")

    # Test for invalid input - special characters
    with pytest.raises(ValueError):
        grade_to_gpa("+")

    with pytest.raises(ValueError):
        grade_to_gpa("A*")

    # Test for invalid input - numeric input
    with pytest.raises(ValueError):
        grade_to_gpa("88")

    with pytest.raises(ValueError):
        grade_to_gpa("9+")


def test_numerical_grade():
    """
    Integer mark (numerical grade) inputs
    """
    assert grade_to_gpa(100) == 4.0
    assert grade_to_gpa(95) == 4.0
    assert grade_to_gpa(90) == 4.0
    
    assert grade_to_gpa(89) == 4.0
    assert grade_to_gpa(87) == 4.0
    assert grade_to_gpa(85) == 4.0

    assert grade_to_gpa(84) == 3.7
    assert grade_to_gpa(82) == 3.7
    assert grade_to_gpa(80) == 3.7

    assert grade_to_gpa(79) == 3.3
    assert grade_to_gpa(78) == 3.3
    assert grade_to_gpa(77) == 3.3

    assert grade_to_gpa(76) == 3.0 
    assert grade_to_gpa(74) == 3.0
    assert grade_to_gpa(73) == 3.0

    assert grade_to_gpa(72) == 2.7
    assert grade_to_gpa(71) == 2.7
    assert grade_to_gpa(70) == 2.7

    assert grade_to_gpa(69) == 0.0
    assert grade_to_gpa(37) == 0.0
    assert grade_to_gpa(0) == 0.0

    # Integer mark (numeric grade) input greater than 100
    with pytest.raises(ValueError):
        grade_to_gpa(101)

    # Integer mark (numeric grade) input less than 0 (i.e. negative grade)
    with pytest.raises(ValueError):
        grade_to_gpa(-1)


def test_wrong_input_type():

    # Float Inputs
    with pytest.raises(TypeError):
        grade_to_gpa(82.5)

    # Boolean Inputs
    with pytest.raises(TypeError):
        grade_to_gpa(True)




