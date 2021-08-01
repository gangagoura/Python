import sys
a = int(sys.stdin.readline())

for i in range(2,a+2,2 ):
    if(i % 2 == 0) and (i <= a):
        print(i)
