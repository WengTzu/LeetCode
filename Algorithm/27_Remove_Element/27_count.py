class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        print(nums.count(val))
        for i in range(nums.count(val)):
            print("remove", i)
            nums.remove(val)
        return len(nums)

a = Solution()
sol = a.removeElement([0,1,2,2,3,0,4,2], 2)
print("solution")
print(sol)