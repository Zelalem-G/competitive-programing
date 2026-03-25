class Solution(object):
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        if n < 2:
            return n

        ans = 1
        l = 0
        inv = None  

        for r in range(n - 1):
            if arr[r] == arr[r+1]:
                l = r + 1
                inv = None
                continue

            cur_dir = 1 if arr[r] > arr[r+1] else -1

            if inv is None:
                inv = cur_dir
            elif cur_dir == inv:
                l = r  
            else:
                inv = cur_dir

            ans = max(ans, r - l + 2)

        return ans