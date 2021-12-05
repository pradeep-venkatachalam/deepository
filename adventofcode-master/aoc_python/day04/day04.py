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
    isFirstBingo = False
    isBoardBingo = [False]*len(mat_boards)
    arr_boards = []
    bingo_sum_first = 0
    bingo_sum_last = 0

    for mat in mat_boards:
        arr_boards.append(flatten(mat))

    for number in callout:
        for bdNr in range(len(arr_boards)):
            arr_boards[bdNr] = [-1 if int(number)==x else x for x in arr_boards[bdNr]]
            if(isNegVector(arr_boards[bdNr]) == True):
                if(isFirstBingo == False):
                    bingo_board_first = arr_boards[bdNr]
                    bingo_number_first = int(number)
                    isFirstBingo = True
                if(isBoardBingo[bdNr] == False):
                    bingo_board_last = arr_boards[bdNr]
                    bingo_number_last = int(number)
                    isBoardBingo[bdNr] = True
        if (isBoardBingo.count(False) == 0):
            break

    for num in bingo_board_first:
        bingo_sum_first += num if num!=-1 else 0
    for num in bingo_board_last:
        bingo_sum_last += num if num!=-1 else 0

    prod_first = bingo_sum_first*bingo_number_first
    prod_last = bingo_sum_last*bingo_number_last

    print(prod_first)
    print(prod_last)

def flatten(Inputstring: str):
    """
    Convert a 2D string Matrix to a integer list
    .split() removes all the whitespaces, tabs and newlines
    list(map()) converts to integer list
    """
    flat = list(map(int, Inputstring.split()))
    return(flat)


def isNegVector(arr_boards: list):
    """
    Convert integer list to numpy matrix 
    Compare against neg vector
    """
    neg_vector = np.array([-1, -1, -1, -1, -1])

    a = np.asarray(arr_boards).reshape(5,5)
    for i in range(5):
        if(np.array_equal(a[i],neg_vector)) or \
            np.array_equal(a[:,i],neg_vector):
            return True


def main():
    """ Main entry point of the app """
    FileOpen()
    part1()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
