class Solution(object):
    def countGood(self, nums, k):
        ans = 0
        pair=0
        l=0
        count = {}
        for r in range(len(nums)):
            if nums[r] in count:
                pair += count[nums[r]]
                count[nums[r]] += 1
            else:
                count[nums[r]] = 1

            while pair >= k:
                ans += (len(nums) - r)
                count[nums[l]] -= 1
                pair -= count[nums[l]]
                l+=1

        return ans