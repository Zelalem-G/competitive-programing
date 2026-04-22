class Solution(object):
    def search(self, nums, target):
        n = len(nums)

        l, r = 0, n-1
        while l<r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        p = l

        if target >= nums[p] and target <= nums[n-1]:
            l, r = p, n-1
        else:
            l, r = 0, p-1

        while l<=r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                return m

        return -1