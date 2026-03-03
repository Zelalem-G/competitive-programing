n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
sub = 0
for i in a:
    if k <= 0:
        break
    if i - sub > 0:
        print(i - sub)
        
        sub = i
        k -= 1

if k > 0:
    print('0\n' * k)