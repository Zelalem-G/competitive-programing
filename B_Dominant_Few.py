for _ in range(int(input())):
  n = int(input())
  players = list(map(int, input().split()))
 
  players.sort(reverse=True)

  won = 0
 
  e = 0
  c = len(players)-2
  crowdSkill = players[-1]+players[-2]
  elitSkill = players[0]

  while e < c:
    if elitSkill > crowdSkill:
      won = 1
      break
    e += 1
    c -= 1
    crowdSkill += players[c]
    elitSkill += players[e]

  if won:
    print("YES")
  else:
    print("NO")