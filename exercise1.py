#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to GPA conversion

This module contains one function grade_to_gpa. The input can be an integer (0-100)
or a letter grade (A+, A, A-, B+, B, B-, or FZ).
All other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if input is not a string or integer
        ValueError if input is out of range
    """

    letter_grade = ""
    gpa = 0.0

    if type(grade) is str:
        # Check that letter grade input is a valid input
        if grade == "A+" or grade == "A" or grade == "A-" or grade == "B+" or grade == "B" \
            or grade == "B-" or grade == "FZ":
            # These are valid letter grade inputs
            letter_grade = grade
        else:
            # If the letter grade input is not valid, raise the ValueError Exception
            raise ValueError("Invalid letter grade input")
    elif type(grade) is int:
        # Check that numerical grade input is in the accepted range
        if (grade >= 0) and (grade <= 100):
            # These are valid numerical grade inputs
            # Assigning corresponding letter grades for GPA assignments
            if grade >= 90:
                letter_grade = "A+"
            elif grade >= 85:
                letter_grade = "A"
            elif grade >= 80:
                letter_grade = "A-"
            elif grade >= 77:
                letter_grade = "B+"
            elif grade >= 73:
                letter_grade = "B"
            elif grade >= 70:
                letter_grade = "B-"
            else:
                letter_grade = "FZ"

        else:
            # If the numerical grade input is not valid, raise the ValueError Exception
            raise ValueError("Invalid numerical grade input")
    else:
        # Raise a TypeError exception
        raise TypeError("Invalid type input")

    # Added by Kyungho Jung
    # If statements to evaluate the letter grade and return the corresponding GPA
    if letter_grade == "A+":
        gpa = 4.0
    elif letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7
    elif letter_grade == "B+":
        gpa = 3.3
    elif letter_grade == "B":
        gpa = 3.0
    elif letter_grade == "B-":
        gpa = 2.7
    elif letter_grade == "FZ":
        gpa = 0.0

    return gpa

