class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        nums = sorted(set(nums))  
        ans = n
        l = 0

        for r in range(len(nums)):
            while nums[r] - nums[l] >= n:
                l += 1

            window = r - l + 1

            ans = min(ans, n - window)

        return ans