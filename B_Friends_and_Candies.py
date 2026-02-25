for _ in range(int(input())):
  n = int(input())
  candies = list(map(int,input().split()))

  sum = 0
  for c in candies:
    sum += c
  
  if n == 1:
    print(0)
  else:
    average = sum // n
    dis = 0
    k =0
    for candy in candies:
      if candy == average:
        continue
      elif candy > average:
        k += 1
        dis += candy - average
      else:
        dis -= average - candy
    
    if dis == 0:
      print(k)
    else:
      print(-1)
