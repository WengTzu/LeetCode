class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin = 
        """nums = sorted(nums1+nums2)
        if len(nums) % 2 == 0:
            index = len(nums) // 2
            index2 = len(nums) // 2 -1
            return float(nums[index] + nums[index2]) / 2
        else:
            return nums[len(nums) // 2]"""
a = Solution()
sol = a.findMedianSortedArrays([1,2], [3,4])
print("solution")
print(sol)