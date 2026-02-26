for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  start = 0

  a.sort()
  for i  in range(n-1):
    if abs(a[i] - a[i+1]) <= 1:
      start += 1
    
  if start == n-1:
    print("YES")
  else:
    print("NO")