class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start] += val
            diff[end + 1] -= val

        for i in range(1, n):
            diff[i] += diff[i - 1]

        res = []
        for i in range(n):
            shift = diff[i] % 26
            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            res.append(new_char)

        return "".join(res)