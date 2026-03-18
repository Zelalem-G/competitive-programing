class Solution:
    def findAnagrams(self, s, p):
        ans = []
        tar = {}

        for c in p:
            tar[c] = tar.get(c,0)+1

        cur = {}
        done = 0
        l = 0

        for r in range(len(s)):
            cur[s[r]] = cur.get(s[r],0)+1

            if s[r] in tar:
                if cur[s[r]] == tar[s[r]]:
                    done += 1
                elif cur[s[r]] == tar[s[r]] + 1:
                    done -= 1

            if r-l+1 > len(p):
                if s[l] in tar:
                    if cur[s[l]] == tar[s[l]]:
                        done -= 1
                    elif cur[s[l]] == tar[s[l]] + 1:
                        done += 1
                cur[s[l]] -= 1
                if cur[s[l]] == 0:
                    del cur[s[l]]
                l += 1

            if done == len(tar):
                ans.append(l)

        return ans