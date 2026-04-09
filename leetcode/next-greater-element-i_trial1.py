class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        mp = {}

        for num in nums2:
            while stack and stack[-1] < num:
                mp[stack.pop()] = num
            stack.append(num)

        for num in stack:
            mp[num] = -1

        ans = []
        for num in nums1:
            ans.append(mp[num])

        return ans