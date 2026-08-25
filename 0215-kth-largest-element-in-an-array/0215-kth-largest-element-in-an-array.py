import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        target = k - 1
        left, right = 0, len(nums) - 1

        while left <= right:

            # Random pivot
            pivot = nums[random.randint(left, right)]

            # 3-way partition
            greater = left
            i = left
            smaller = right

            while i <= smaller:

                if nums[i] > pivot:
                    nums[greater], nums[i] = nums[i], nums[greater]
                    greater += 1
                    i += 1

                elif nums[i] < pivot:
                    nums[i], nums[smaller] = nums[smaller], nums[i]
                    smaller -= 1

                else:
                    i += 1

            # [left ... greater-1]  > pivot
            # [greater ... smaller] == pivot
            # [smaller+1 ... right] < pivot

            if target < greater:
                right = greater - 1

            elif target > smaller:
                left = smaller + 1

            else:
                return pivot