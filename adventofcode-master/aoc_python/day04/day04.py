#!/usr/bin/env python3
"""
Day 4 of Advent of Code 2021
"""

__author__ = "Pradeep Venkatachalam"
__version__ = "0.1.0"

import numpy as np

def FileOpen():
    data = open("input.txt", "r").read().split('\n\n')
    callout = data[0].split(',')
    boards = data[1:]
    return callout, boards

def part1():
    callout, mat_boards = FileOpen()
    num_boards = len(mat_boards)
    isBoardAlreadyBingo = [False]*num_boards
    arr_boards = []
    winner = {
        "bingo_board": [],
        "bingo_number": [],
        "bingo_sum": [],
        "products": [],
    }

    for mat in mat_boards:
        # Convert board (str) matrixes to board (int) list
        arr_boards.append(flatten(mat))

    for number in callout:
        for bdNr in range(num_boards):
            arr_boards[bdNr] = mark(number,arr_boards[bdNr])
            if(isNegVector(arr_boards[bdNr]) == True and isBoardAlreadyBingo[bdNr] == False):
                    # Adds Valid Board to list if board not bingoed yet
                    winner["bingo_board"].append(arr_boards[bdNr])
                    winner["bingo_number"].append(int(number))
                    isBoardAlreadyBingo[bdNr] = True

    for idx in range(len(winner["bingo_board"])):
        winner["bingo_sum"].append(addBingoMat(winner["bingo_board"][idx]))
        winner["products"].append(MultMatandNum(winner["bingo_sum"][idx],winner["bingo_number"][idx]))

    print(winner["products"][0])
    print(winner["products"][-1])

def addBingoMat(bingo_list: list):
    """
    Add unmarked numbers in bingo matrix
    """
    return(sum([x for x in bingo_list if x!=-1]))

def MultMatandNum(bingo_sum: int, bingo_number: int ):
    return(bingo_sum*bingo_number)

def mark(n, board):
    """
    Mark occurence of number in board with -1
    """
    return [-1 if int(n)==x else x for x in board]

def flatten(Inputstring: str):
    """
    Convert a 2D string Matrix to a integer list
    .split() removes all the whitespaces, tabs and newlines
    list(map()) converts to integer list
    """
    return(list(map(int, Inputstring.split())))


def isNegVector(arr_boards: list):
    """
    Convert integer list to numpy matrix 
    Compare against sum
    """
    a = np.asarray(arr_boards).reshape(5,5)
    return(True if(any(sum(a)== -5) or any(sum(a.T)==-5)) else False)

def main():
    """ Main entry point of the app """
    FileOpen()
    part1()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
