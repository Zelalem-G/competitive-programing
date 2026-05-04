class Solution(object):
    def smallestDivisor(self, nums, threshold):
        
        def can(d):
            total = 0
            for n in nums:
                total += (n + d - 1) // d
            return total <= threshold

        l, r = 1, max(nums)

        while l < r:
            m = (l + r) // 2

            if can(m):
                r = m
            else:
                l = m + 1

        return r