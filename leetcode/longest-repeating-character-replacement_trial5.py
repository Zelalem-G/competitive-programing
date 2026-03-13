from collections import Counter
class Solution(object):
    def characterReplacement(self, s, k):
        ans = 0
        l,r=0,0
        max_val = 0
        window = Counter()
        
        while r < len(s):
            window[s[r]] += 1
            max_val = max(max_val,window[s[r]])

            while (r-l+1)-max_val > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                
                l += 1
            ans = max(ans, r-l+1)
            r += 1

        return ans