#!/usr/bin/env python3
"""
Day 2 of Advent of Code 2021
"""

__author__ = "Pradeep Venkatachalam"
__version__ = "0.1.0"

import sys

def FileOpen():
    a = []
    with open("input.txt") as input_file:
        for line in input_file:
            a.append(int(line))
    return a, len(a)

def part1():
    a, length = FileOpen()

def part2():
    a, length = FileOpen()

def main():
    """ Main entry point of the app """
    print("Hello World")
    FileOpen()
    part1()
    part2()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
