class Solution(object):
    def arrangeCoins(self, n):
        add = 0
        row = 1
        ans = 0

        while add + row <= n:
            add += row
            ans += 1
            row += 1

        return ans