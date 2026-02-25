for _ in range(int(input())):
  n = int(input())
  timers = list(map(int,input().split()))

  sortedTimers =  [0]*n
  mp = {}

  for i in range(n):
    sortedTimers[i] = timers[i]
    mp[i] = timers[i]

  sortedTimers.sort()

  t = sortedTimers[0]-1

  
