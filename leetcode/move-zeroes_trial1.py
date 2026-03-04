class Solution(object):
    def moveZeroes(self, nums):
        ph , se = 0 ,0

        while se < len(nums):
            if nums[se] != 0:
                nums[se], nums[ph] = nums[ph],nums[se]
                ph += 1
                
            se += 1
            
        