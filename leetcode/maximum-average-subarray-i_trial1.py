class Solution(object):
    def findMaxAverage(self, nums, k):
        ans = 0
        for i in range(k):
            ans += nums[i]

        l = 0
        r = k

        window = ans

        while r < len(nums):
            window = window - nums[l] + nums[r]
            ans = max(window, ans)
            l += 1
            r += 1
        
        return ans / float(k)