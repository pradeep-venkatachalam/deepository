#!/usr/bin/env python3
"""
Day 7 of Advent of Code 2021
"""

__author__ = "Pradeep Venkatachalam"
__version__ = "0.1.0"

import numpy as np
import statistics



def FileOpen():
    mappings = open("input.txt", "r").read().split(',')
    return mappings

def part1(mapping):
    sum = 0
    input_mapping = list(map(int, mapping))
    median =  int(statistics.median(input_mapping))

    for val in input_mapping:
        sum += abs(val - median)
    print(sum)

def part2(mapping):
    sum = 0
    weight = 0
    sum_list = []
    median_list = []

    input_mapping = list(map(int, mapping))
    min_input = min(input_mapping)
    max_input = max(input_mapping)

    for median in range (min_input, max_input):
        sum = 0
        for val in input_mapping:
            distance = abs(val - median)
            weight = ((distance)*(distance+ 1))/2
            sum += abs(weight)
        sum_list.append(sum)
        median_list.append(median)

    index_min = np.argmin(sum_list)
    print(sum_list[index_min], median_list[index_min])
    

def main():
    """ Main entry point of the app """
    mapping = FileOpen()
    # part1(mapping)
    part2(mapping)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()