class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        pair = 0
        ans = 1
        l = 0

        for r in range(1, len(s)):
            if s[r] == s[r-1]:
                pair += 1

            while pair >= 2:
                if s[l] == s[l+1]:
                    pair -= 1
                l += 1

            ans = max(ans, r-l+1)

        return ans