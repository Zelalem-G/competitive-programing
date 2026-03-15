for _ in range(int(input())):
  n = int(input())
  shoes = list(map(int, input().split())) 
  ans = [0]*n
  won = 1
  a = 1

  l,r = 0,0
  while l<r:
    while shoes[l] == shoes[r]:
      r += 1
    if r-l == 1:
      won = 0
      break
    for i in range(r-1,l-1,-1):
      ans[j]= i
      l=r

  if won:
    print(*ans)
  else:
    print(-1)
  