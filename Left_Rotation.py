def rotateLeft(d, arr):
    # Write your code here
    ans = [0]* len(arr)
    for i in range(len(arr)):
        if d == len(arr):
            d = 0
        ans[i] = arr[d]
        d += 1
        
    return ans