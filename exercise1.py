#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to GPA conversion

This module contains one function grade_to_gpa. The input can be an integer mark (numerical grade) (0-100)
or a letter grade (A+, A, A-, B+, B, B-, or FZ). All other inputs will result in an error.

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
    Converts a given grade input into the equivalent UofT Graduate Students GPA.
    Grade inputs may be letter grades or integer marks (numerical grades).

    :param:
        grade (integer or string): Grade to be converted into GPA
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value will be between 0.0-4.0

    :raises:
        TypeError if input is not a string or integer
        ValueError if input is out of range
    """

    letter_grade = ""
    gpa = 0.0

    if type(grade) is str:
        valid_letter_grade_array = ["A+", "A", "A-", "B+", "B", "B-", "FZ"]

        # Check that letter grade input is a valid input by comparing with array
        if grade in valid_letter_grade_array:
            # These are valid letter grade inputs
            letter_grade = grade
        else:
            # If the letter grade input is not valid, raise the ValueError Exception
            raise ValueError("Invalid letter grade input")
    elif type(grade) is int:
        letter_grade = mark_to_letter(grade)

    else:
        # Raise a TypeError exception
        raise TypeError("Invalid type input")

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


def mark_to_letter(mark):
    """
    Return the corresponding letter grade for a given integer mark (numerical grade).

    :param:
        mark (integer or string): Grade to be converted into GPA
            Accepted values are 0-100.

    :return:
        string : Letter grade that corresponds to integer mark (numerical grade) input

    :raises:
        ValueError if integer mark (numerical grade) input is out of range
    """

    letter_grade_to_be_returned = ""
    # Check that integer mark (numerical grade) input is in the accepted range
    if (mark >= 0) and (mark <= 100):

       # Assign corresponding letter grades for GPA assignments
        if mark >= 90:
            letter_grade_to_be_returned = "A+"
        elif mark >= 85:
            letter_grade_to_be_returned = "A"
        elif mark >= 80:
            letter_grade_to_be_returned = "A-"
        elif mark >= 77:
            letter_grade_to_be_returned = "B+"
        elif mark >= 73:
            letter_grade_to_be_returned = "B"
        elif mark >= 70:
            letter_grade_to_be_returned = "B-"
        else:
            letter_grade_to_be_returned = "FZ"
    else:
       # If the integer mark (numerical grade) input is not valid, raise the ValueError Exception
        raise ValueError("Invalid integer mark (numerical grade) input")

    return letter_grade_to_be_returned