class Solution(object):
    def getAverages(self, nums, k):
        ans = [-1]*len(nums)
        for i in range(1,len(nums)):
            nums[i] = nums[i-1]+nums[i]

        cur = 0
        for r in range(len(nums)):
            if r-k >=0 and r+k<len(nums):
                if r-k == 0:
                    total = nums[r+k]
                else:
                    total = nums[r+k] - nums[r-k-1]
                ans[r] = total // (2*k + 1)
            else:
                ans[r] = -1

        return ans