class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        new  = []
        for i in range(len(nums)):
            ans.append(nums[i])
            new = nums + ans
        return new