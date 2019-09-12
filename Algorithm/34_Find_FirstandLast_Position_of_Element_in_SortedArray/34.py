class Solution(object):
    def searchRange(self, nums, target):
        """
        :type s: str
        :rtype: int
        """
        first = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]

if __name__ == '__main__':
    a = Solution()
    sol = a.searchRange(nums = [5,7,7,8,8,10], target = 8)
    print("solution")        
    print(sol)