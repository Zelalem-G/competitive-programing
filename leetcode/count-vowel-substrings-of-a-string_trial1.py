from collections import Counter

class Solution(object):
    def countVowelSubstrings(self, word):
        vowels = set("aeiou")
        count = 0
        n = len(word)

        for l in range(n):
            cur = Counter()
            seen = 0

            for r in range(l, n):
                c = word[r]

                if c not in vowels:
                    break  

                if cur[c] == 0:
                    seen += 1
                cur[c] += 1

                if seen == 5:
                    count += 1

        return count