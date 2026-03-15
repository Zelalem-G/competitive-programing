for _ in range(int(input())):
  n = int(input())
  script = list(input())

  l = 0
  r = n-1

  a = -1
  b = -1

  while l < n and r >= 0:
    if script[l] == "A" and a == -1:
      a = l

    if script[r] == "B" and b == -1:
      b = r

    if a > -1 and b > -1:
       break
    
    l += 1
    r -= 1

  if a == -1 or b == -1 or a > b:
    print(0)
  else:
    print(b-a)