#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * n
    for i in queries:
        a, b, k = i
        arr[a - 1] += k
        if b <= n-1:
            arr[b] -= k
    maxn = 0
    sum = 0
    print(arr)
    for i in arr:
        sum += i
        if sum > maxn:
            maxn = sum
    return maxn


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)
