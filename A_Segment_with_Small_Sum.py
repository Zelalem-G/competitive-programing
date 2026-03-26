n, s = map(int, input().split())
a = list(map(int, input().split()))
ans=0

l=0
cur=0
for r in range(n):
  cur+=a[r]

  while cur >s:
    cur-= a[l]
    l+=1

  if cur<=s:
    ans = max(ans,r-l+1)

print(ans)
