class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        sq = sorted(x * x for x in nums)

        return sum(sq[n // 2:]) - sum(sq[:n // 2])