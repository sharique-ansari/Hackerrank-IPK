#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    prev = ''
    out = 0
    for j in s:
        if j == prev:
            i = s.index(j)
            s = s[:i] + s[i + 1:]
            out += 1
        prev = j
    return out


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
