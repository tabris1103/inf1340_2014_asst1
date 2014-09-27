#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

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
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade = ""
    gpa = 0.0

    if type(grade) is str:
        # check that the grade is one of the accepted values
        if grade == "A+" or grade == "A" or grade == "A-" or grade == "B+" or grade == "B" \
            or grade == "B-" or grade == "FZ":
            # These are valid letter grade inputs
            letter_grade = grade
        else:
            # If the passed string is not a proper letter grade, then it will raise the ValueError Exception
            raise ValueError("Invalid letter grade input")
    elif type(grade) is int:
        print("mark") # remove this line once the code is implemented
        # check that grade is in the accepted range
        if (grade >= 0) and (grade <= 100):
            # These are valid numerical grade inputs
            # Assigning corresponding letter grade for GPA
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
            # If the passed grade is not a proper numerical grade, then it will raise the ValueError Exception
            raise ValueError("Invalid numerical grade input")
    else:
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter")

    # Added by Kyungho Jung
    # If statement to evaluate the current letter grade
    # and return the appropriate GPA scale.
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

