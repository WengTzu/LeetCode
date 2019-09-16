class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type s: str
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            print(i, nums[i])
            if target > nums[i] and target <= nums[i+1]:
                return i+1
                print("min:", i)

if __name__ == '__main__':
    a = Solution()
    sol = a.searchInsert([1,3,5,6], 7)
    print("solution")        
    print(sol)