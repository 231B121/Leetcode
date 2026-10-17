class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def digSum(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        arr = [(nums[i], i) for i in range(n)]

        arr.sort(key=lambda x: (digSum(x[0]), x[0]))

        pos = [0] * n

        for i in range(n):
            pos[arr[i][1]] = i

        fix = [False] * n
        swaps = 0

        for i in range(n):
            if fix[i]:
                continue

            j = i
            count = 0

            while not fix[j]:
                fix[j] = True
                j = pos[j]
                count += 1

            if count > 1:
                swaps += count - 1

        return swaps