for _ in range(int(input())):
    n = int(input())
    shoes = list(map(int, input().split()))
    
    ans = [0]*n
    won = True

    l = 0

    while l < n:
        r = l
        while r < n and shoes[r] == shoes[l]:
            r += 1
        
        if r - l == 1:
            won = False
            break
        
        for i in range(l, r-1):
            ans[i] = i + 2
        ans[r-1] = l + 1
        
        l = r

    if won:
        print(*ans)
    else:
        print(-1)