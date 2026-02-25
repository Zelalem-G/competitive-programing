for _ in range(int(input())):
  n, m = map(int,input().split())

  houses = list(map(int,input().split()))
  greatest = max(houses)    
  ans = [0]*m
  a = 0

  for _ in range(m):
    c, l, r = input().split()
    l = int(l)
    r = int(r)

    if greatest >= l and greatest <= r:
      if c == "+":
        greatest += 1
      else:
        greatest -= 1

    ans[a] = greatest
    a += 1

  print(*ans)