class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type strs: List[str]
        :rtype: str
        [""] - indeed have a string ""
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[-1]

        for i in range(len(nums)-2):
            print(i, nums[i])
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(total - target) < abs(result - target):
                    result = total
                if total == target:
                    return target
                elif total > target:
                    r -= 1
                else: # total < target
                    l += 1
        return result
        #nums = [-4, -1, 1, 2]


a = Solution()
sol = a.threeSumClosest([-1, 2, 1, -4], 1)
print("solution")
print(sol)