from collections import deque
def reverse_index(n,k):
    for i in range(n):
        x = a.popleft() if i%2 else a.pop()
        if x==k: return i

for _ in range(int(input())):
    n,k = map(int,input().split())
    a = deque(range(n))
    print(reverse_index(n,k))
