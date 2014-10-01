#!/usr/bin/env python3

"""
    Verifies that the digits of a UPC code are correct by performing a checksum
    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum(upc):
    """
    Verifies that the digits of a UPC are correct by performing checksum

    :param upc: a 12-digit Universal Product Code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    is_correct_upc_code = False

    # Verify that the type of input is valid
    if type(upc) is str:
        # Verify that the length of string is valid
        if len(upc) != 12:
            raise ValueError("Length of the UPC input is not equal to 12")

        # Verify that the UPC input does not contain any characters or strings
        elif str(upc).isnumeric() is False:
            raise ValueError("UPC code must not contain any string/character values")
        else:
            # Convert string to array
            upc_array = list(upc)
            check_sum = 0

            # Generate checksum using the first 11 digits of the UPC input
            for string_index in range(0, 11):
                if string_index % 2 == 0:
                    check_sum += int(upc_array[string_index]) * 3
                    print("Check Sum at " + str(string_index) + " = " + str(check_sum))
                else:
                    check_sum += int(upc_array[string_index])
                    print("Check Sum at " + str(string_index) + " = " + str(check_sum))

            # Calculate modulo 10 of check_sum
            mod_10_of_check_sum = check_sum % 10

            # Subtract mod_10_of_check_sum from 10 to get the supposed last digit
            subtracting_from_10 = 10 - mod_10_of_check_sum

            # Compare the supposed last digit with the the actual twelfth digit
            # Return True if they are equal, False otherwise
            last_digit = int(upc_array[11])
            if subtracting_from_10 == last_digit:
                is_correct_upc_code = True
    else:
        # raise TypeError if not string
        raise TypeError("The UPC input is not string type")

    return is_correct_upc_code
