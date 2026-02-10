n = int(input())
s = input()

target = "ACTG"

def dist(a, b):
    d = abs(ord(a) - ord(b))
    return min(d, 26 - d)

ans = float('inf')

for i in range(n - 3):
    cost = 0
    for j in range(4):
        cost += dist(s[i + j], target[j])
    ans = min(ans, cost)

print(ans)
