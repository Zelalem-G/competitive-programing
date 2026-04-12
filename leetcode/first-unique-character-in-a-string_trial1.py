class Solution(object):
    def firstUniqChar(self, s):
        freq = [0]*26

        for c in s:
            i = ord(c) - ord("a")
            freq[i] += 1

        for i in range(len(s)):
            idx = ord(s[i]) - ord("a")
            if freq[idx] == 1:
                return i

        return -1