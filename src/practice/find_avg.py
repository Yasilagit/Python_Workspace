#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = list(map(int, input().split()))
    

    def avg(nums):
        total = 0
        for i in range(0, len(nums), 1):
            total += nums[i]
        return total / len(nums)

    res = avg(nums)

    fptr.write('%.2f' % res + '\n')

    fptr.close()
