combatNumYoussef, totaltimeYoussef = map(int,input().split())
won = True

for _ in range(int(input())):
  curCombat, curTime = map(int,input().split())
  if curCombat > combatNumYoussef:
    won = False
    break
  elif curCombat == combatNumYoussef and totaltimeYoussef > curTime:
    won = False
    break
  
if won:
  print("The Champion Saves the Accused")
else:
  print("The Fallen Champion")

