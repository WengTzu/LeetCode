import collections
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) < 4:
            return result
        nums.sort()
        for i in range(len(nums)-3):
            print(i)
            if i > 0 and nums[i] == nums[i-1]:
                print("continue")
                continue
            for j in range(i+1, len(nums) - 2):
                print("j",j)
                if j > i+1 and nums[j] == nums[j-1]:
                    print("continue j")
                    continue
                low = j + 1
                high = len(nums) -1
                while low < high:
                    print(i, j, low, high)
                    sum = nums[i] + nums[j] + nums[low] + nums[high]
                    if sum == target:
                        result.append([nums[i], nums[j], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif sum < target:
                        low += 1
                    else:
                        high -= 1
        return result
            
            
a = Solution()
sol = a.fourSum([1, 0, -1, 0, 0, -2, 2], 0)
#-2, -1, 0, 0, 0, 1, 2
print("solution")
print(sol)