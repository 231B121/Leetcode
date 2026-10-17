class Solution(object):

    def minSwaps(self, nums):
        
        arr = sorted(nums, key=lambda x: (self.digitSum(x), x))
        
        index_di = {num : i for i, num in enumerate(nums)}

        count = 0 

        for i in range(len(nums)):
            if nums[i] != arr[i]:

                j = index_di[arr[i]]

                nums[i], nums[j] = nums[j], nums[i]

                index_di[nums[j]] = j
                index_di[nums[i]] = i

                count += 1

        return count

    
    def digitSum(self, n):

        sum = 0

        while n > 0:
            sum += n % 10
            n //= 10
        
        return sum