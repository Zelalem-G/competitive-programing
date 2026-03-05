def countingSort(arr):
    # Write your code here
    count = [0]*100
    for n in arr:
        count[n] += 1
    return count
