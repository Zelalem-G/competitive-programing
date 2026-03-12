from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        ans =[0,float("inf")]
        target = Counter(t)
        window = Counter()
        l=0
        req,cur = len(target),0

        for r in range(len(s)):
            window[s[r]] += 1

            if window[s[r]] == target[s[r]]:
                cur += 1

            while cur == req:
                if r-l+1 < ans[1]-ans[0]+1:
                    ans[0] = l
                    ans[1] = r
                ch = s[l]
                l += 1
                window[ch] -= 1
                if window[ch] < target[ch]:
                    cur -= 1
                if window[ch] == 0: del window[ch]
            
        return "" if ans[1] == float("inf") else s[ans[0]:ans[1]+1]

        