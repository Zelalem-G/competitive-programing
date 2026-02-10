t = int(input())

for _ in range(t):
    n,m,p,q = map(int,input().split())
    
    total = 0
    
    block = n//p
    r = n % p
    
    if r == 0:
        total = block * q
        if total == m:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")