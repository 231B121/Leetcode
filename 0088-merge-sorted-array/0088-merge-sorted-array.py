class Solution:
    def merge(self, nums1, m, nums2, n):
        ans = []
        i = j = 0

        

        while i < m:
            ans.append(nums1[i])
            i += 1

        while j < n:
            ans.append(nums2[j])
            j += 1
        

        nums1[:] = sorted(ans)