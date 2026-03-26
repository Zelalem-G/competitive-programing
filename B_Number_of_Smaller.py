n,m = map(int,input().split())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))
ans = [0]*m

a=0
cur=0
for b in range(m):
  while a<n and arr[a]<brr[b]:
    a+=1
    cur=a
  ans[b] = cur

print(*ans)