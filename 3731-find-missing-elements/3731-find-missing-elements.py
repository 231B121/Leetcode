from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []

        left = 0
        right = 1

        while right < len(nums):
            curr = nums[left] + 1

            while curr < nums[right]:
                ans.append(curr)
                curr += 1

            left += 1
            right += 1

        return ans