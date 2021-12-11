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
    for day in range(len_days):
        input_mapping = Day(input_mapping)
        if (day%7 ==0):
            print (day, len(input_mapping), input_mapping)
    print(len(input_mapping))

def rotate(l, n):
    return l[n:] + l[:n]
 

def part2(mapping, len_days):
    # Value of Lifetime of fish can be from 0-8
    # Initialize 9 input array
    count_array = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    input_mapping = list(map(int, mapping))
    for fish in input_mapping:
        count_array[fish] += 1
    
    for i in range(len_days):
        count_array = rotate(count_array,1)
        count_array[6] += count_array[8]

    print(sum(count_array))

def main():
    """ Main entry point of the app """
    mapping = FileOpen()
    len_days = 256

    part2(mapping, len_days)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
