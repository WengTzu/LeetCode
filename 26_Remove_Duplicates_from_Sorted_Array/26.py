class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        count = 0
        for i in range(len(nums)):
            print(nums[count], nums[i])
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
            #print(i)
        return count+1
a = Solution()
sol = a.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print("solution")
print(sol)