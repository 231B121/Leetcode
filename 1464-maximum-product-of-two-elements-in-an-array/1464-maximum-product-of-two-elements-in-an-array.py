class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest1 = largest2 = float('-inf')

        for num in nums:
            if num >= largest1:
                largest2 = largest1
                largest1 = num
            elif num > largest2:
                largest2 = num

        return (largest1 - 1) * (largest2 - 1)