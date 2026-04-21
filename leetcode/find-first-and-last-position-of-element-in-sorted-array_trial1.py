class Solution(object):
    def searchRange(self, nums, target):
        def findLeft():
            l, r = 0, len(nums) - 1
            ans = -1
            
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
                
                if nums[m] == target:
                    ans = m
            
            return ans

        def findRight():
            l, r = 0, len(nums) - 1
            ans = -1
            
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
                
                if nums[m] == target:
                    ans = m
            
            return ans

        return [findLeft(), findRight()]