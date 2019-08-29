class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1+nums2)
        if len(nums) % 2 == 0:
            index = len(nums) // 2
            index2 = len(nums) // 2 -1
            return float(nums[index] + nums[index2]) / 2
        else:
            return nums[len(nums) // 2]
        """print(len(nums1))
        print(len(nums2))
        print((len(nums1) + len(nums2)) / 2, (len(nums1) + len(nums2)) // 2)
        if((len(nums1) + len(nums2)) / 2 - (len(nums1) + len(nums2)) // 2 ) > 0:
            print("0....")
            index =  (len(nums1) + len(nums2)) // 2 
            print(index)
            if(index > len(nums1)):
                return nums2[index-nums1]
            else:
                return nums1[index]
        else:
            print("123")"""
a = Solution()
sol = a.findMedianSortedArrays([1,2], [3,4])
print("solution")
print(sol)