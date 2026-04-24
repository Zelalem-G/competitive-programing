class Solution(object):
    def countGoodNumbers(self, n):
        MOD = 10**9 + 7

        def power(base, exp):
            result = 1
            base %= MOD

            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp //= 2

            return result

        even = (n + 1) // 2
        odd = n // 2

        return (power(5, even) * power(4, odd)) % MOD