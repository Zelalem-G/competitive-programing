from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a)
    
    for i in freq:
        if freq[i] % 2 == 1:
            print("YES")
            return
    print("NO")

t = int(input())
for _ in range(t):
    solve()