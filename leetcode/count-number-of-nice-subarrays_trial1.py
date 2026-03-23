class Solution:
    def numberOfSubarrays(self, nums, k):
        ans = 0
        l = 0
        count = 0
        end = 0
        
        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                count += 1
                end = 0
            
            while count == k:
                end += 1
                
                if nums[l] % 2 == 1:
                    count -= 1
                l += 1
            
            ans += end
            
        return ans