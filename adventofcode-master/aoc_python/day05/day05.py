#!/usr/bin/env python3
"""
Day 4 of Advent of Code 2021
"""

__author__ = "Pradeep Venkatachalam"
__version__ = "0.1.0"

import numpy as np

source = []
dest = []
x, y = 0,1
plot = np.zeros((1000,1000))

def FileOpen():
    print("hello World")
    mappings = open("input.txt", "r").read().split('\n')

    for entry in mappings:
        a = entry.split('->')
        s = list(map(int, a[0].split(',')))
        d = list(map(int, a[1].split(',')))
        source.append(s)
        dest.append(d)

    for sc,dc in zip(source,dest):
        min_x, min_y = min(sc[x],dc[x]), min(sc[y],dc[y])
        max_x, max_y = max(sc[x],dc[x]), max(sc[y],dc[y])

        dist = abs(sc[y] - dc[y])
        if (slope(sc,dc)==1) :
            for step in range(dist+1):
                plot[min_x+step, min_y+step] += 1
        if (slope(sc,dc)==-1) :
            for step in range(dist+1):
                plot[max_x-step, min_y+step] += 1

        length = abs(sc[y] - dc[y]) + abs(sc[x] - dc[x])
        if (sc[y]) == (dc[y]):
            for step in range(length+1):
                plot[min_x+step, sc[y]] += 1
        if (sc[x]) == (dc[x]):            
            for step in range(length+1):
                plot[sc[x], min_y+step] += 1
    
    num_targets = (plot >= 2).sum()
    print(num_targets)

def slope(sc,dc):
    if((sc[x] - dc[x]) == (sc[y] - dc[y])):
        return(1)
    if((sc[x] - dc[x]) == -1*(sc[y] - dc[y])):
        return(-1)

def main():
    """ Main entry point of the app """
    FileOpen()
    # part1()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
