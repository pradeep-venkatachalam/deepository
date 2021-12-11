#!/usr/bin/env python3
"""
Day 8 of Advent of Code 2021
"""

__author__ = "Pradeep Venkatachalam"
__version__ = "0.1.0"

import numpy as np

def FileOpen():
    mapping = open("input.txt", "r").read().split('\n')
    return mapping

def part1(mapping):
    segments = ['a','b','c','d','e','f','g']
    mt1,mt4,mt7,mt8,mt235,mt069 = [],[],[],[],[],[]
    sum = 0
    for line in mapping:
        whole = line.replace(' | ',' ').split(' ')

        for word in whole:
            if len(word) == 2:
                mt1.append(word)
            elif len(word) == 4:
                mt4.append(word)
            elif len(word) == 3:
                mt7.append(word)
            elif len(word) == 7:
                mt8.append(word)
            elif len(word) == 6:
                mt069.append(word)
            elif len(word) == 5:
                mt235.append(word)

        hex0 = inbnotina(mt1[0],mt7[0])
        for word in mt069:
            if inaandb(word, mt4[0]) == 4: #(Isolate 9)
                hex4 = inbnotina(word, segments) #(9 vs 8)
            if (inaandb(word, mt1[0]) == 1): #(Isolate 6)
                hex2 = inbnotina(word, mt8[0]) #(6 vs 8)
        hex5 = inbnotina(hex2, mt1[0])

        for word in mt235:
            if inaandb(word, mt4[0]) == 2: #(Isolate 2)
                hex1 = inbnotina(word+hex5, segments)
        hex3 = inbnotina(mt1[0] + hex1 ,mt4[0])
        hex6 = inbnotina(mt4[0] + hex0 + hex4 ,mt8[0])

        str = ["","","","","","","","","",""]
        str[0] = (''.join(sorted((hex0+hex1+hex2+     hex4+hex5+hex6))))
        str[1] = (''.join(sorted((          hex2+          hex5     ))))
        str[2] = (''.join(sorted((hex0+     hex2+hex3+hex4+     hex6))))
        str[3] = (''.join(sorted((hex0+     hex2+hex3+     hex5+hex6))))
        str[4] = (''.join(sorted((hex1+     hex2+hex3+     hex5     ))))
        str[5] = (''.join(sorted((hex0+hex1+     hex3+     hex5+hex6))))
        str[6] = (''.join(sorted((hex0+hex1+     hex3+hex4+hex5+hex6))))
        str[7] = (''.join(sorted((hex0+     hex2+          hex5     ))))
        str[8] = (''.join(sorted((hex0+hex1+hex2+hex3+hex4+hex5+hex6))))
        str[9] = (''.join(sorted((hex0+hex1+hex2+hex3+     hex5+hex6))))

        post = line.split('| ')[1]
        words = post.split(' ')
        number = 0

        for word in words:
            compare = ''.join(sorted(word))
            for idx,val in enumerate(str):
                if (compare == val):
                    number = idx+(10*number)
        sum +=number
    print(sum)

#                             0000 
#                            1    2
#                            1    2
# mapping reference           3333 
#                            4    5
#                            4    5
#                             6666

def inbnotina(str1, segments):
    for i in segments:
        if str1.count(i) == 0:
            missing = i
    return(missing)


def inaandb(str1, str2):
    res = set(str1).intersection(str2)
    return(len(res))

def main():
    """ Main entry point of the app """
    mapping = FileOpen()
    part1(mapping)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()