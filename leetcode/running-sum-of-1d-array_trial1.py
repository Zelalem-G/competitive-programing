class Solution(object):
    def runningSum(self, nums):
        ans = [0]*len(nums)
        cur = 0
        for i in range(len(nums)):
            ans[i] = cur+nums[i]
            cur += nums[i]
        return ans
        