t = int(input())

for _ in range(t):
  n,k = map(int,input().split(" "))
  health = list(map(int, input().split()))
  position = list(map(int, input().split()))

  monsters = [0] * (n + 1)

  for i in range(n):
    monsters[abs(position[i])] += health[i]

  cur=0
  res = "YES"
  for i in range(1,n+1):
    cur += k
    if monsters[i] > cur: 
       res = "NO"
       break
    else:
      cur -= monsters[i]
  
  print(res)