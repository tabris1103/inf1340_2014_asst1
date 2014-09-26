#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum (upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    is_correct_upc_code = False

    # check type of input
    if type(upc) is str:
        # check length of string
        if len(upc) != 12:
            # raise ValueError if not 12
            raise ValueError("Length of the passed parameter is not equal to 12")
        else:
            # convert string to array
            # hint: use the list function

            upc_array = upc.list
            for letter in upc_array:
                print("Hello")

            # generate checksum using the first 11 digits provided
            # check against the the twelfth digit

            # return True if they are equal, False otherwise
            is_correct_upc_code = False
    else:
        # raise TypeError if not string
        raise TypeError("Passed parameter is not string type")

    return is_correct_upc_code

