class Solution:
    def maxVowels(self, s, k):
        l = 0
        c = 0
        ans = 0
        vowels = set("aeiou")

        for r in range(len(s)):
            if s[r] in vowels:
                c += 1

            if (r-l+1) == k:
                ans = max(ans, c)

                if s[l] in vowels:
                    c -= 1
                l += 1

        return ans