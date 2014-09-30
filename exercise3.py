#!/usr/bin/env python3

""" Assignment 1, Exercise 3, INF1340, Fall, 2014. Rock, Paper, Scissors.

This module contains a function called decide_rps. This function returns the result of the game

Example:
    $ python exercise3.py

"""

def decide_rps(player1_choice, player2_choice):
    """
    Returns the results of the Rock, Paper, Scissors game.

    :param:
        player1_choice, player2_choice (string): choices made by player1_choice and player2
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
    valid_input_array = ["R", "P", "S"]
    if type(player1_choice) is str and type(player2_choice) is str:
        if player1_choice not in valid_input_array:
            # raise the ValueError Exception If the input for player 2 is not valid,
            raise ValueError("Invalid player1 input - Enter 'R' for Rock, 'P' for Paper, 'S' for Scissors.")
        elif player2_choice not in valid_input_array:
            # raise the ValueError Exception If the input for player 2 is not valid,
            raise ValueError("Invalid player2 input - Enter 'R' for Rock, 'P' for Paper, 'S' for Scissors.")
    else:
        # Raise a TypeError exception
        raise TypeError("Invalid input type -  Enter 'R' for Rock, 'P' for Paper, 'S' for Scissors.")

    # Define dictionary variable that contains the player1 winning combination
    # key = Player 1 choice : Value = Player 2's losing choice
    choice_combinations_for_player1_wins = {"R": "S", "P": "R", "S": "P"}

    # Look up choices input values in dictionary and return game result

    # Default Result set to tie
    result = 0

    # check whether game ties or not.
    # if game doesn't tie, then check whether player 1 wins by comparing player2's
    # choice with corresponding values in dictionary
    # If value is not found in the dictionary, then it means player 2 wins.
    if player1_choice == player2_choice:
        result = 0
    else:
        if choice_combinations_for_player1_wins[player1_choice] == player2_choice:
            result = 1
        else:
            result = 2

    return result

