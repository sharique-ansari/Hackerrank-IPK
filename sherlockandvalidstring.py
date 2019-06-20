#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the isValid function below.
def isValid(s):
    dic = Counter(s)
    li = list(dic.values())
    li.sort()
    if li.count(li[0]) == len(li) or ((li[-1] - li[-2]) == 1 and li.count(li[0]) == len(li)-1):
        return "YES"
    elif li.count(li[-1]) == len(li)-1 and li[0] ==1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    # fptr.write(result + '\n')
    #
    # fptr.close()
