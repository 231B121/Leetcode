class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        n = len(nums)
        arr = [1] * n

        for i in range(n):
            arr[i] = prefix
            prefix *= nums[i]

        for i in range(n-1 ,-1,-1):
            arr[i] *= suffix
            suffix *= nums[i]
        return arr

        
        