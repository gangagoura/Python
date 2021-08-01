def persons():
    N = int(input())
    x = input().split()
    for i in range(N):
        x[i] = int(x[i])
    lowest = min(x)
    y = x.index(lowest) + 1
                        
    return y
                  
print(persons()) 
