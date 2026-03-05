from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        freq = Counter(s)
        ans  = ""

        sorted_freq = sorted(freq.items(), key=lambda item:item[1],reverse=True)

        for c,v in sorted_freq:
            for i in range(v,0,-1):
                ans += c

        return ans