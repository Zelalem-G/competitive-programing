for _ in range(int(input())):
  n,s,x = map(int, input().split())
  arr = list(map(int, input().split()))

  total = sum(arr)
  won = 0

  while s >= total:
    if s == total:
      won = 1
      break
    
    s -= x
  
  if won:
    print("YES")
  else:
    print("NO")