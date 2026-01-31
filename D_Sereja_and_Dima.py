from collections import deque

n = int(input())
dq = deque(map(int, input().split(" ")))

siraji = 0
dima = 0

while len(dq):
  if dq[0] > dq[-1]:
    siraji += dq.popleft()
  else:
    siraji += dq.pop()

  if len(dq) == 0:
    break

  if dq[0] > dq[-1]:
    dima += dq.popleft()
  else:
    dima += dq.pop()

print(siraji, dima)