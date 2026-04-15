from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        maxD = deque()
        minD = deque()
        
        left = 0
        res = 0
        
        for right in range(len(nums)):
            while maxD and nums[maxD[-1]] < nums[right]:
                maxD.pop()
            maxD.append(right)
            
            while minD and nums[minD[-1]] > nums[right]:
                minD.pop()
            minD.append(right)
            
            while nums[maxD[0]] - nums[minD[0]] > limit:
                left += 1
                
                if maxD[0] < left:
                    maxD.popleft()
                if minD[0] < left:
                    minD.popleft()
            
            res = max(res, right - left + 1)
        
        return res