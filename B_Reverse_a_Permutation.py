t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    suffix_max = [0]*n
    suffix_max[-1] = p[-1]

    for i in range(n-2, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], p[i])

    l = -1
    for i in range(n):
        if suffix_max[i] > p[i]:
            l = i
            break

    if l == -1:
        print(*p)
        continue

    r = l
    for i in range(l, n):
        if p[i] == suffix_max[l]:
            r = i

    p[l:r+1] = reversed(p[l:r+1])
    print(*p)