class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, e1 in enumerate(nums):
            if e1 == target:
                return i
        return -1 
        
                

if __name__ == '__main__':
    a = Solution()
    sol = a.search([1,2,3,6,5], 0)
    print("solution")        
    print(sol)