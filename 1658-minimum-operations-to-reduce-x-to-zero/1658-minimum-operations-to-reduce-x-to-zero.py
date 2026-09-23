class Solution:
    def minOperations(self, nums, x):
        n = len(nums)
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1

        if target == 0:
            return n

        left = 0
        s = 0
        longest = -1

        for right in range(n):

            s += nums[right]

            while left <= right and s > target:
                s -= nums[left]
                left += 1

            if s == target:
                longest = max(longest, right - left + 1)

        return -1 if longest == -1 else n - longest