class Solution:
    def containsDuplicate(self, nums):
        hash_map = {}

        for num in nums:
            if num in hash_map:
                return True

            hash_map[num] = 1

        return False