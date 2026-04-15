class Solution(object):
    def isPowerOfThree(self, n):
        def helper(x):
            if x == 1:
                return True
            if x <= 0 or x % 3 != 0:
                return False
            return helper(x // 3)

        return helper(n)