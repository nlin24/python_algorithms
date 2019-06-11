#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    track = None
    mountain = 0
    valley = 0
    for i in range(n):
        if i == 0:
            track = level
            if s[i] == "U":
                level += 1
            elif s[i] == "D":
                level -= 1
        else:
            track = level
            if s[i] == "U":
                level += 1
            elif s[i] == "D":
                level -= 1
            if level == 0 and track > level:
                mountain += 1
            elif level == 0 and track < level:
                valley += 1
    return valley
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
