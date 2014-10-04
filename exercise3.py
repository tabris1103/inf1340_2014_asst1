#!/usr/bin/env python3

""" Assignment 1, Exercise 3, INF1340, Fall, 2014. Rock, Paper, Scissors.

This module contains a function called decide_rps.
This function returns the result of a game of Rock, Paper, Scissors between player1 and player2.

Example:
    $ python exercise3.py

"""

__author__ = 'Kyungho Jung & Christine Oh'
__status__ = "Completed"

def decide_rps(player1_choice, player2_choice):
    """
    Returns the results of the Rock, Paper, Scissors game.

    :param:
        player1_choice, player2_choice (string): choices made by player1 and player2
            Accepted values for choice inputs are "R" for Rock, "P" for Paper, and "S" for Scissors

    :return:
        int: The results of the game
            If player1 wins, return 1.
            If player2 wins, return 2.
            If it is a tie game, return 0.

    :raises:
        TypeError if choice input is not a string
        ValueError if choice input is is not "Rock", "Paper", or "Scissors".
    """

    # Define valid choice inputs
    valid_input_array = ["Rock", "Paper", "Scissors"]
    if type(player1_choice) is str and type(player2_choice) is str:
        if player1_choice not in valid_input_array:
            # Raise the ValueError Exception if the input for player1 is not valid,
            raise ValueError("Invalid player1 input - Enter 'Rock' for Rock, 'Paper' for Paper, 'Scissors' for Scissors.")
        elif player2_choice not in valid_input_array:
            # Raise the ValueError Exception if the input for player2 is not valid,
            raise ValueError("Invalid player2 input - Enter 'Rock' for Rock, 'Paper' for Paper, 'Scissors' for Scissors.")
    else:
        # Raise a TypeError exception
        raise TypeError("Invalid input type -  Enter 'Rock' for Rock, 'Paper' for Paper, 'Scissors' for Scissors.")

    # Define dictionary variable that contains choice combination resulting in a win for player1
    # Key = player1's winning choice : Value = player2's losing choice
    choice_combinations_for_player1_wins = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}

    # Look up choice input values in dictionary and return game result

    # Default result set to tie
    result = 0

    # Check whether game ties or not.
    # If game does not result in a tie, check whether player1 wins by comparing player2's
    # choice with corresponding values in dictionary.
    # If value is not found in the dictionary, player2 must win.
    if player1_choice == player2_choice:
        result = 0
    else:
        if choice_combinations_for_player1_wins[player1_choice] == player2_choice:
            result = 1
        else:
            result = 2

    return result

