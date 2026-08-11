class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        gourav =  set()
        for abhi in nums:
            if abhi in gourav:
                return True
            gourav.add(abhi)
        return False
        

        