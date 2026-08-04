class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        mn = min(nums)
        mx = max(nums)

        ans = []
        for i in range(mn + 1, mx):
            if i not in s:
                ans.append(i)

        return ans