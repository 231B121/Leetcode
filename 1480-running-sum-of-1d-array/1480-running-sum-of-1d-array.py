class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num = 0
        ans = [] 
        for i in range(n):
            num += nums[i]
            ans.append(num)
        return ans

                
        return num

        