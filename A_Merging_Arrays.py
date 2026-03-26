n,m = map(int,input().split())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))

ans = []
a = b = 0

while a < n and b < m:
    if arr[a] <= brr[b]:
        ans.append(arr[a])
        a += 1
    else:
        ans.append(brr[b])
        b += 1

while a < n:
    ans.append(arr[a])
    a += 1
while b < m:
    ans.append(brr[b])
    b += 1

print(*ans)