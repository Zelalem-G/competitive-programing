for _ in range(int(input())):
  n,p = map(int,input().split())
  totalNums = list(map(int,input().split()))
  costs = list(map(int,input().split()))

  ans = 0
  lowIdx = 0
  for i in range(n):
    if costs[i] < p and costs[i] < costs[lowIdx]:
      lowIdx = i
  direct = n - totalNums[lowIdx]

