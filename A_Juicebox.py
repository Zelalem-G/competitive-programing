for _ in range(int(input())):
  n, k = map(int, input().split())
  juice = [0]*(k+1)
  ans = 0

  for i in range(k):
    brand, cost = map(int, input().split())
    juice[brand] += cost 

  sortedJuices = sorted(juice, reverse=True)

  ans = sum(sortedJuices[:n])
  print(ans)