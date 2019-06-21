#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the commonChild function below.
def commonChild(s1, s2):
    output = 0
    l = len(s1)
    m = len(s2)
    dptable = [[0 for i in range(l + 1)] for j in range(m + 1)]

    # pre fill the trivial values in DP table

    for i in range(l + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dptable[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dptable[i][j] = dptable[i - 1][j - 1] + 1
                output = max(output, dptable[i][j])
            else:
                dptable[i][j] = max(dptable[i][j-1], dptable[i-1][j])
    return output


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
