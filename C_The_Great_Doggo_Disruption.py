n = int(input())
pupies = input()

pupCount = [0]*27
won = 0

for p in pupies:
  pupCount[ord(p)-ord("a")] += 1
  if pupCount[ord(p)-ord("a")] >= 2:
    won = 1
    break

if won or n == 1:
  print("Yes")
else:
  print("No")
