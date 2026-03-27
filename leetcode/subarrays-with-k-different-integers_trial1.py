class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        return self.atMost(nums, k) - self.atMost(nums, k-1)

    def atMost(self, nums, k):
        count = {}
        l = 0
        ans = 0

        for r in range(len(nums)):
            if nums[r] not in count:
                count[nums[r]] = 0
            count[nums[r]] += 1

            while len(count) > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1

            ans += (r-l+1)

        return ans