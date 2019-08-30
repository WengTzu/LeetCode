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
                j = i + 1
                while j < L and nums[j] > nums[i-1]:
                    j += 1
                print("i=", i, "j=",j)
                nums[i-1], nums[j-1] = nums[j-1], nums[i-1]
                print(nums)
                nums[i:] = nums[L - 1: i - 1: -1]
                print(nums)
                return
        nums.reverse()

if __name__ == '__main__':
    a = Solution()
    sol = a.nextPermutation([1,2,2,3,2,1])
    print("solution")        
    print(sol)