n = int(input())
a = list(map(int, input().split()))

even = 0
odd = 0

for num in a:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

if even > 0 and odd > 0:
    a.sort()

print(*a)