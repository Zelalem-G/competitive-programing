class Solution(object):
    def countPairs(self, nums, t):
        nums.sort()
        count=0
        l=0
        r=1
        while l<len(nums)-1:
            if nums[l]+nums[r]<t:
                r+=1
                count += 1
            else:
                l+=1
                r=l+1
            if r==len(nums):
                l+=1
                r=l+1

        return count        