w = int(input())

if w <4:
    print("NO")
else:
    if w % 2 == 0:
        print("YES")
    else:
        a = (w-1) // 2
        b = ((w-1) // 2)+1
        if a % 2 == 0 and b % 2 == 0:
            print("YES")
        else:
            print("NO")