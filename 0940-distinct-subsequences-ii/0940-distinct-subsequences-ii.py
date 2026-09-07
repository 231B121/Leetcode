class Solution:
    def distinctSubseqII(self, s: str) -> int:

        MOD = 10 ** 9 + 7

        hash = [0] * 26

        distinct_count = 1

        for ch in s:

            previous_count = distinct_count

            pos = ord(ch) - ord('a')

            distinct_count = (2 * distinct_count - hash[pos]) % MOD

            hash[pos] = previous_count

        return (distinct_count - 1) % MOD

        
        