class Solution:
    def findAnagrams(self, s, p):
        ans = []
        tar = {}

        for c in p:
            tar[c] = tar.get(c,0)+1

        cur = {}
        l = 0

        for r in range(len(s)):
            cur[s[r]] = cur.get(s[r],0)+1

            if r-l+1 > len(p):
                cur[s[l]] -= 1
                if cur[s[l]] == 0:
                    del cur[s[l]]
                l += 1

            if cur == tar:
                ans.append(l)

        return ans