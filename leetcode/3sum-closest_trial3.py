class Solution(object):
    def threeSumClosest(self, nums, t):
        nums.sort()
        ans= float("inf")
        for i in range(len(nums)-2):
           l=i+1
           r=len(nums)-1

           while l<r:
            cur = nums[i]+nums[l]+nums[r]
            if cur == t:
                return cur
            elif abs(t-cur)<abs(t-ans):
                ans = cur
            if cur < t:
                l += 1
            else:
                r -= 1

        return ans