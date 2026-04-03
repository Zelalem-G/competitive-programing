class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()

        prev = 0

        for i in range(len(arr)):
            if arr[i] > prev + 1:
                arr[i] = prev + 1
            
            prev = arr[i]

        return prev