n = int(input())
pupies = input()

pupCount = [0]*27 #a-z 0-26 
won = 0  

for p in pupies:
  i = ord(p)-ord("a")
  pupCount[i] += 1
  if pupCount[i] >= 2:
    won = 1
    break

if won or n == 1: 
  print("Yes")
else:
  print("No")



n = int(input())
s = input()

if len(set(s)) < len(s) or n == 1:
    print("Yes")
else:
    print("No")