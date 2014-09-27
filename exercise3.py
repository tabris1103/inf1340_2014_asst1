#!/usr/bin/env python3

""" Assignment 1, Exercise 3, INF1340, Fall, 2014. Rock, Paper, Scissors.

This module contains a function called decide_rps. This function returns the result of the game

Example:
    $ python exercise3.py

"""

def decide_rps(player1, player2):
    """
    Returns the results of the Rock, Paper, Scissors game.

    :param:
        player1, player2 (string): choices made by player1 and player2
            Accepted values are "R" for Rock, "P" for Paper, and "S" for Scissors

    :return:
        int: The results of the game
            If player 1 wins, return 1.
            If player 2 wins, return 2.
            If it is a tie game, return 0.

    :raises:
        TypeError if input is not a string
        ValueError if input is is not "R", "P", or "S".
    """

    # Define valid inputs
    if type(player1) is str and type(player2) is str:
        if (player1 == "R") or (player1 == "P") or (player1 == "S"):
            # These are valid player1 inputs
        else:
            # If the input is not valid, raise the ValueError Exception
            raise ValueError("Invalid player1 input")
        if (player2 == "R") or (player2 == "P") or (player2 == "S"):
            # These are valid player2 inputs
        else:
            # If the input is not valid, raise the ValueError Exception
            raise ValueError("Invalid player2 input")
    else:
        # Raise a TypeError exception
        raise TypeError("Invalid type input - Enter 'R' for Rock, 'P' for Paper, 'S' for Scissors.")

    # Define choices and corresponding results in dictionary
    choice_combinations = {}
    choice_combinations["RR"] = 0
    choice_combinations["RP"] = 2
    choice_combinations["RS"] = 1
    choice_combinations["PR"] = 1
    choice_combinations["PP"] = 0
    choice_combinations["PS"] = 2
    choice_combinations["SR"] = 2
    choice_combinations["SP"] = 1
    choice_combinations["SS"] = 0

    # Assign input values to "choices" variable
    choices = (player1 & player2)
    if choices in choice_combinations:
        result = choice_combinations[choices]
    else:
        # Raise a ValueError Exception
        raise ValueError("choices input not found in choice_combinations dictionary.")

    return result

