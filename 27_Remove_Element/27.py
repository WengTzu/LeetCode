

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        front, last = 0, len(nums) - 1

        while front <= last:
            print("front, last", front, last)
            print(nums[front], nums[last])
            if nums[front] == val:
                nums[front], nums[last] = nums[last], nums[front]
                last -= 1
            else:
                front += 1
            print("front, last", front, last)
            print(nums[front], nums[last])
            print(nums)
        return last + 1

a = Solution()
sol = a.removeElement([1], 1)
print("solution")
print(sol)