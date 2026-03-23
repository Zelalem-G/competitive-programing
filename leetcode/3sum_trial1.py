class Solution(object):
    def threeSum(self, nums):
        if len(nums)<3:
            return []
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i+1
            r = len(nums)-1
            t = -nums[i]
            while l<r:
                v = nums[l]+nums[r]
                if v>t:
                    r-=1
                elif v<t:
                    l+=1
                else:
                    a= [nums[i],nums[l],nums[r]]
                    ans.append(a)
                    while l+1<r and nums[l] == nums[l + 1]: l += 1
                    while r-1>i and nums[r] == nums[r - 1]: r -= 1
                    l += 1
                    r -= 1

        return ans