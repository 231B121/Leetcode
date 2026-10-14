class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
     
        a = sorted(x * x for x in nums)

        k = len(nums) // 2   

        return sum(a[k:]) - sum(a[:k])