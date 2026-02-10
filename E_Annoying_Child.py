import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    even = []
    maxOdd = 0 

    for num in a:
        if num % 2:
            maxOdd = max(maxOdd, num)
        else: 
            even.append(num)

    sumEven = sum(even) 

    lastEvenFirstOdd = even[-1] if even else maxOdd

    if not maxOdd:
        print(" ".join(["0"]*n) + "\n")
        continue
    
    print(str(maxOdd) + " ")
    lastNum = maxOdd 

    e = 0

    for i in range(2, n+1):
        if i > len(even) + 1: 

            if (i - (len(even)+1)) % 2: 

                print("0 ") if i == n else print(str(sumEven+maxOdd-lastEvenFirstOdd) + " ")
            else:
                print(str(sumEven+maxOdd) + " ")

        else: 
            lastNum += even[e]
            print(str(lastNum) + " ")
            e += 1

    print("\n")
