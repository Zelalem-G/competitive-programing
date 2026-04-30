class Solution(object):
    def nextGreatestLetter(self, letters, target):
        l, r = 0, len(letters) - 1

        while l <= r:
            m = (l + r) // 2

            if letters[m] <= target:
                l = m + 1
            else:
                r = m - 1

        return letters[l % len(letters)]