#!/usr/bin/env python3
"""
Day 3 of Advent of Code 2021
"""

__author__ = "Pradeep Venkatachalam"
__version__ = "0.1.0"

import sys

thisdict = {
  "direction": "Ford",
  "magnitude": "Mustang"
}

def FileOpen():
    master_list = []
    list = []
    count1 =     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
    list_one =[]
    list_zero =[]

    with open("measurements.csv") as input_file:
        for line in input_file:
            master_list.append(line)
    list = master_list
    for j in range(12):
        list_one = []
        list_zero = []
        count1 =     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
        for i in range(len(list)):
            if(list[i][j] == '1'):
                count1[j] += 1
                list_one.append(list[i])
            else:
                count1[j] += 0
                list_zero.append(list[i])
        if(len(list_one)>=len(list_zero)):
            list = list_one
        else:
            list = list_zero
        if(len(list)==1):
            break
        
    print(list)
    a=int(list[0],2)
    print(a)

    list = master_list
    for j in range(12):
        list_one = []
        list_zero = []
        count1 =     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
        for i in range(len(list)):
            if(list[i][j] == '1'):
                count1[j] += 1
                list_one.append(list[i])
            else:
                count1[j] += 0
                list_zero.append(list[i])
        if(len(list_one)<len(list_zero)):
            list = list_one
        else:
            list = list_zero        
        if(len(list)==1):
            break
    
    print(list)
    b=int(list[0],2)
    print(b)
    print(a*b)

def main():
    """ Main entry point of the app """
    FileOpen()
    # part1()
    # part2()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()