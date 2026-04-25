
class Solution(object):
    def guessNumber(self, n):
        l = 1
        r = n

        while l <= r:
            m = (l + r) // 2
            res = guess(m)

            if res == 0:
                return m
            elif res == 1:
                l = m + 1
            else:
                r = m - 1