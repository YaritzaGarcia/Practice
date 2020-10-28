import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    jumps = 0
    n = len(c)
    if(n >= 2 and n <= 100):
        oldPos = 1
        oldOldPos = 1
        zeros = False
        for pos in c[:n-1]:
            if(pos == 0 and (oldPos == 1 or oldOldPos == 1)):
                jumps += 1
                zeros = False
                oldOldPos = oldPos
                oldPos = pos
            elif(pos == 0 and oldPos == 0 and oldOldPos == 0 and not zeros):
                jumps += 1
                zeros = True
                oldOldPos = oldPos
                oldPos = pos
            elif(pos == 0 and oldPos == 0 and oldOldPos == 0 and zeros):
                zeros = False
                oldOldPos = oldPos
                oldPos = pos
            else:
                oldOldPos = oldPos
                oldPos = pos

    return jumps


print(jumpingOnClouds([
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]))
