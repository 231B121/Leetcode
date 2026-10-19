class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        sor = sorted(nums)
        j = []

        for i in range(len(sor)):
            if sor[i] == target:
                j.append(i)

            if sor[i] > target:
                break

        return j