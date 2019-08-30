class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        print("len",len(nums))
        for i in range(L-1, 0, -1):
            print(i, nums[i])
            if nums[i] > nums[i-1]:
                print("small")
                

if __name__ == '__main__':
    a = Solution()
    sol = a.nextPermutation([1,2,3,6,5])
    print("solution")        
    print(sol)