for _ in range(int(input())):
  n = int(input())
  target = list(map(int,input().split()))

  play = 0

  uniqe = set(target)

  if len(uniqe) == 1:
    print(1)
  elif len(uniqe) == 2:
    print(3)
  else:
    r = (len(uniqe)*2)-1
    print(r)