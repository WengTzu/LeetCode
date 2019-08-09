class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in nums:
            for j in range(nums.count(i)-1):
                nums.remove(i)
        return len(nums)
a = Solution()
sol = a.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print("solution")
print(sol)