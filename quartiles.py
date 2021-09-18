#!/bin/python3

import math
import os
import random
import re
import sys
#from statistics import median
#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def median(arr):
    if len(arr)%2 == 0:
        return int(sum(arr[len(arr)//2-1:len(arr)//2+1])/2)
    else:
        return arr[len(arr)//2]
def quartiles(n,arr):
    # Write your code here
    from statistics import median
    q1 = (int(median(arr[:len(arr)//2])))
    q2 = (int(median(arr)))
    #q3 = (int(median(arr[(n+1)//2:])))
    if n%2 == 0:
        q3 = median(arr[len(arr)//2:])
    else:
        q3 = median(arr[len(arr)//2+1:])
    return q1, q2, int(q3)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = sorted([int(num) for num in input().split()])

    res = quartiles(n, data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
