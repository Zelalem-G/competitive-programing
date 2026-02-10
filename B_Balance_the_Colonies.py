t = int(input())

for _ in range(t):
    n = int(input())
    if n < 4:
        print(n)
    elif n%2:
        print(1)
    else:
        print(0) 