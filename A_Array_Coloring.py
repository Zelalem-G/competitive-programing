for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    mpRed = {}
    mpBlue = {}
    
    for i in range(n):
        if i % 2:
            mpRed[arr[i]] = i
        else:
            mpBlue[arr[i]] = i
    
    arr.sort()
    
    no = True
    prev = arr[0]
    for i in range(1,n):
        if arr[i] in mpRed and prev in mpRed:
            print("NO")
            no = False
            break
        elif arr[i] in mpBlue and prev in mpBlue:
            print("NO")
            no = False
            break
        else:
            prev = arr[i]

    if no:
        print("YES")