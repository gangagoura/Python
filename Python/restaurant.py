import math

def best(x,y):
    prod = x*y
    for i in range(2,int(math.sqrt(prod))+1)[::-1]:
        if not x%i and not y%i:
            return x*y//i**2
    else:
        return prod
for _ in range(int(input())):
    x,y = list(map(int,input().split()))
    print(best(x,y))
