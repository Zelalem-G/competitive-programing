class Solution(object):
    def twoSum(self, numbers, target):
        ans = [0,0]

        l,r = 0 ,len(numbers)-1

        while l<r:
            added = numbers[l]+numbers[r]
            if added > target:
                r -= 1
            elif added < target:
                l += 1
            else:
                ans[0] = l+1
                ans[1] = r+1
                break
        return ans
        