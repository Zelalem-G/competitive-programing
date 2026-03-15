class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        l=0
        r= len(nums)-1
        ans = 0

        while l<r:
            added = nums[l]+nums[r]
            if added <k:
                l += 1
            elif added > k:
                r -= 1
            else:
                ans += 1
                l += 1
                r -= 1
                
        return ans