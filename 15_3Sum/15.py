class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [] 
        n = len(nums)
        #while / for
        # [0, 1, 2, 3, 4, 5, ...]
        # if nums[0] + nums[1] + nums[2] > 0 : return []
        
        # [-100, 0, 1, 2, 3, ..., 8, 9]
        # nums[0] + nums[-1] + nums[-2] < 0 
        print(nums)
        for i in range(n-2):
            print(i, nums[i])
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[-1] + nums[-2] < 0:
                print(nums[i] , nums[-1] , nums[-2])
                print("continue")
                continue
            if i > 0 and nums[i] == nums[i-1]:
                print("i == i-1", nums[i], nums[i-1])
                continue
            l = i+1
            r = n-1
            while l < r:
                print("i,l,r",i, l, r)
                total = nums[i] + nums[l] + nums[r]
                print(total, "=", nums[i], nums[l], nums[r])
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while nums[l] == nums[l+1] and l+1 < r:
                        l += 1
                    l += 1
                    while nums[r] == nums[r-1] and l < r-1:
                        r -= 1
                    r -=1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return result
            
a = Solution()
sol = a.threeSum([-1, 0, 1, 2, -1, -4])
print("solution")
print(sol)