class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s)<2:
            return len(s)
        l = 0
        r = 1
        ans = 0

        while r < len(s):
            n = s.find(s[r],l,r)
            if n != -1:
                l = n+1
            ans = max(ans, r-l+1)
            r += 1
        
        return ans