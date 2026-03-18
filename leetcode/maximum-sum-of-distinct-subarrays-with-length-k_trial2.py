class Solution:
    def maximumSubarraySum(self, nums, k):
        ans = 0
        cur = 0
        freq = {}
        l = 0

        for r in range(len(nums)):
            cur += nums[r]
            freq[nums[r]] = freq.get(nums[r], 0) + 1

            while freq[nums[r]] > 1:
                freq[nums[l]] -= 1
                cur -= nums[l]
                l += 1

            if r - l + 1 > k:
                freq[nums[l]] -= 1
                cur -= nums[l]
                l += 1

            if r - l + 1 == k:
                ans = max(ans, cur)

        return ans