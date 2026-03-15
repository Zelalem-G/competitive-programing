def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort()
    res = 0
    i = 0
    j = 0
    while i < len(a):
        if j < len(b):
            if b[j] <= n - i:
                res += sum(a[i:i + b[j] - 1])
                i += b[j]
                j += 1
            else:
                res += sum(a[i:])
                break
        else:
            res += sum(a[i:])
            break
    print(res)

t = int(input())
for _ in range(t):
    solve()