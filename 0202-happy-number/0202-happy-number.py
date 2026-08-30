class Solution:
    def isHappy(self, n):

        seen = set()

        while n != 1:

            if n in seen:
                return False

            seen.add(n)

            happy = 0

            while n > 0:
                digit = n % 10
                happy += digit * digit
                n //= 10

            n = happy

        return True