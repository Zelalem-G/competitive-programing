class Solution(object):
    def checkSubarraySum(self, nums, k):
        prefix_mod = 0
        seen = {0: -1}  

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in seen:
                if i - seen[prefix_mod] >= 2:
                    return True
            else:
                seen[prefix_mod] = i

        return False