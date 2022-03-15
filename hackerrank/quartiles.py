#!/bin/python3

import math
import os
import random
import re
import sys

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = sorted(list(map(int, input().split())))
from statistics import median
print(int(median(x[:n//2])))
print(int(median(x)))
print(int(median(x[(n+1)//2:])))
