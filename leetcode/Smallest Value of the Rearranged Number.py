class Solution(object):
    def smallestNumber(self, num):
        if num == 0:
            return 0

        negative = num < 0
        digits = list(str(abs(num)))

        if not negative:
            digits.sort()

            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], digits[0]
                        break

            result = int("".join(digits))
        else:
            digits.sort(reverse=True)
            result = int("".join(digits)) * -1

        return result
