for _ in range(int(input())):
  n, m = map(int, input().split())
  cards = []

  for i in range(n):
    row = list(map(int, input().split())) 
    cards.append(row)

  if n == 1 and m == 1:
    print(-1)
  else:
    for i in range(1,n+1):
      row = []
      for j in range(m):
        if i == n:
          if j+1 >= m:
            row.append(cards[0][0])
          else:
            row.append(cards[0][j+1])
        else:
          if j+1 >= m:
            # print(j)
            row.append(cards[i][0])
          else:
            row.append(cards[i][j+1])
      print(*row)
    