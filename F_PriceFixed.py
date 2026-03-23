dict1 = {}
for _ in range(int(input())):
    x, y = map(int, input().split())
    dict1[y] = dict1.get(y, 0) + x

count = sorted(dict1.keys())

i, j = 0, len(count) - 1
rub, cnt = 0, 0

while i <= j:
    if count[i] <= cnt:
        rub += dict1[count[i]]
        cnt += dict1[count[i]]
        i += 1
    else:
        exp = count[i]
        diff = min(exp - cnt, dict1[count[j]])
        rub += 2 * diff
        cnt += diff
        dict1[count[j]] -= diff
        
        if dict1[count[j]] == 0:
            j -= 1

print(rub)