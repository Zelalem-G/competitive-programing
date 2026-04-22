class Solution(object):
    def minEatingSpeed(self, piles, h):

        def canEat(v):
            total = 0
            for p in piles:
                total += (p + v - 1) // v
            return total <= h

        l = 1
        r = max(piles)

        while l < r:
            m = (l + r) // 2
            if canEat(m):
                r = m
            else:
                l = m + 1

        return l