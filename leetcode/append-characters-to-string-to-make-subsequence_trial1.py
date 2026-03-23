class Solution(object):
    def appendCharacters(self, s, t):
        i =0
        for c in s:
            if i < len(t) and c == t[i]:
                i += 1

        return len(t)-i  
        