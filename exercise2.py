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
            raise ValueError("Length of the passed parameter is not equal to 12")

        # checking whether UPC code contains any character or string in it.
        elif str(upc).isnumeric() is False:
            raise ValueError("UPC code must not contain any string/character value")
        else:
            # convert string to array
            upc_array = list(upc)
            check_sum = 0

            # generate checksum using the first 11 digits provided
            for string_index in range(0,11):
                if string_index % 2 == 0:
                    check_sum += int(upc_array.pop(0)) * 3
                    print("Check Sum at " + str(string_index) + " = " + str(check_sum))
                else:
                    check_sum += int(upc_array.pop(0))
                    print("Check Sum at " + str(string_index) + " = " + str(check_sum))

            #Calculate modulo 10 of check_sum
            mod_10_of_check_sum = check_sum % 10

            #subtract mod_10_of_check_sum from 10 to get the calculated last digit
            subtracting_from_10 = 10 - mod_10_of_check_sum

            # check calculated last digit against the the twelfth digit
            # return True if they are equal, False otherwise
            last_digit = int(upc_array.pop(0))
            if subtracting_from_10 == last_digit:
                is_correct_upc_code = True
    else:
        # raise TypeError if not string
        raise TypeError("Passed parameter is not string type")

    return is_correct_upc_code
