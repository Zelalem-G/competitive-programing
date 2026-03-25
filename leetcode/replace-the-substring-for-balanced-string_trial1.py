from collections import Counter

class Solution(object):
    def balancedString(self, s):
        n = len(s)
        t = n // 4
        cur = Counter(s)

        # already balanced
        if all(cur[c] == t for c in "QWER"):
            return 0

        ans = n
        l = 0

        for r in range(n):
            cur[s[r]] -= 1  

            while l < n and all(cur[c] <= t for c in "QWER"):
                ans = min(ans, r - l + 1)
                cur[s[l]] += 1  #
                l += 1

        return ans