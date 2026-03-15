class Solution(object):
    def findContentChildren(self, g, s):
        s.sort()
        g.sort()
        
        ans = 0  # 7 8 9 10
        j,i=0,0

        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
                ans += 1
                j += 1
                i += 1
            else:
                j += 1
        
        return ans