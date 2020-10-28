#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    # Write your code here
    stepsUpLevel = 0
    levelSoFar = 0
    lastLevel = 0
    if(steps >= 2 and steps <= 1000000):
        for step in path:
            lastLevel = levelSoFar
            if(step == "D"):
                levelSoFar -= 1
            elif(step == "U"):
                levelSoFar += 1

            if(lastLevel < 0 and levelSoFar >= 0):
                stepsUpLevel += 1

    return stepsUpLevel
