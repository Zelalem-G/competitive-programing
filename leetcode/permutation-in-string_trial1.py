from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        target = Counter(s1)
        cur = Counter(s2[:len(s1)])
        if cur == target:
            return True
        l=0
        for r in range(len(s1),len(s2)):
            cur[s2[l]] -= 1
            if cur[s2[l]] == 0:
                del cur[s2[l]] 

            cur[s2[r]] += 1
            if cur == target:
                return True

            l += 1
            
        
        return False