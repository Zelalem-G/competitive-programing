n = int(input())

mp = {}
rcr = 0

for _ in range(n):
  m = int(input())

  for i in range(m):
    message = input()
    mp[message] = mp.get(message,0)+1

for message in mp:

  rcr =  (mp[message]/n) * 100
  if rcr >= 80:
    break

if rcr >= 80:
  print("YES")
else:
  print("NO")
  