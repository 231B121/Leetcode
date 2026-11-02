class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mid = nums[n // 2]
        list1 = []
        for items in nums:
            list1.append(abs(items - mid))
        return sum(list1)      