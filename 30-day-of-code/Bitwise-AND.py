#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    maxValue = 0
    check = 0
    for i in range(n-1,0,-1):
        for j in range(n,i,-1):
            tmp = i&j
            if ((tmp > maxValue)&(tmp < k)):
                maxValue = tmp
                if (maxValue + 1 == k):
                    check = 1
                    break
        if (check == 1):
            break
    print maxValue
