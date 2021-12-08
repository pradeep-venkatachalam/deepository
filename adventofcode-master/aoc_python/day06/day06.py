#!/usr/bin/env python3
"""
Day 6 of Advent of Code 2021
"""

__author__ = "Pradeep Venkatachalam"
__version__ = "0.1.0"

import numpy as np



def FileOpen():
    mappings = open("input.txt", "r").read().split(',')
    return mappings

def Day(input_mapping : list):
    append_list = []
    for idx,_ in enumerate(input_mapping):
        input_mapping[idx] = input_mapping[idx] - 1
        if(input_mapping[idx] == -1):
            append_list.append(8)
            input_mapping[idx] = 6

    return (input_mapping+append_list)

def part1(mapping, len_days):
    input_mapping = list(map(int, mapping))
    for _ in range(len_days):
        input_mapping = Day(input_mapping)
    print(len(input_mapping))

def main():
    """ Main entry point of the app """
    mapping = FileOpen()
    len_days = 18

    part1(mapping, len_days)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
