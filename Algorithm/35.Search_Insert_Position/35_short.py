class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type s: str
        :rtype: int
        """
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

if __name__ == '__main__':
    a = Solution()
    sol = a.searchInsert([1,3,5,6], 5)
    print("solution")        
    print(sol)