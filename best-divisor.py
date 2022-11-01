def divisors(n):
    for i in range(1,n+1):
        if not n%i:
            yield i
    
def bestDivisor(n):
    bestNum = 0
    bestSum = 0
    for i in divisors(n):
        s = sum(map(int,str(i)))
        if s == bestSum: 
            bestNum =  min(bestNum,i)
        elif s > bestSum:
            bestNum = i
            bestSum = s
    return bestNum

n = int(input())
print(bestDivisor(n))
