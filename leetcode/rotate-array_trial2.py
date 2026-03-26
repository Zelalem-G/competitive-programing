class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        
        ans = [0]*n
        s = (n - k) % n  

        for i in range(n):
            ans[i] = nums[s]
            s += 1
            if s == n:
                s = 0
                
        for i in range(n):
            nums[i] = ans[i]