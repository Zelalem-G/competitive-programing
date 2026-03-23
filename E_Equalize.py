import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    l = 0
    ans = 0
    
    for r in range(n):
        while a[r] - a[l] > n - 1:
            l += 1
        ans = max(ans, r - l + 1)
    
    print(ans)