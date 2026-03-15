n = int(input())

cards = list(map(int, input().split()))

l = 0
r = len(cards)-1
turn = 0
ans = [0,0]

while l<=r:
  if cards[l] > cards[r]:
    ans[turn] += cards[l]
    l += 1
  else:
    ans[turn] += cards[r]
    r -= 1

  turn = 1-turn

print(*ans)