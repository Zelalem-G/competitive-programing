for _ in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))

  a.sort()
  smallest = float('inf')

  for i in range(n-2):
    smallest = min(abs(a[i+2]-a[i]),smallest)

  print(smallest)