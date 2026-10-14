class Solution:
    def maxAlternatingSum(self, nums):
        n = len(nums)

        for i in range(n):
            nums[i] *= nums[i]

        nums.sort()
        ans = 0

        for i in range(n // 2):
            ans -= nums[i]

        for i in range(n // 2, n):
            ans += nums[i]

        return ans