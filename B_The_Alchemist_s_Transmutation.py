for _ in range(int(input())):
  n = int(input())
  a = list(map(int,input().split()))
  x = int(input())

  smallest = a[0]
  largest = a[0]

  for v in a:
    if v < smallest:
      smallest = v
    if v > largest:
      largest = v

  if smallest <= x <= largest:
    print("YES")
  else:
    print("NO")