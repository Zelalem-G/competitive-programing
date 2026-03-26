class Solution(object):
    def productExceptSelf(self, nums):
        preLeft = [0]*len(nums)
        preLeft[0] = nums[0]

        preRight = [0]*len(nums)
        preRight[len(nums)-1] = nums[-1]

        for i in range(1,len(nums)):
            preLeft[i] = preLeft[i-1]*nums[i]
        for i in range(len(nums)-2,-1,-1):
            preRight[i] = preRight[i+1]*nums[i]

        ans = [0]*len(nums)
        ans[0] = preRight[1]
        ans[-1] = preLeft[-2]

        for i in range(1,len(nums)-1):
            ans[i] = preLeft[i-1]*preRight[i+1]

        return ans