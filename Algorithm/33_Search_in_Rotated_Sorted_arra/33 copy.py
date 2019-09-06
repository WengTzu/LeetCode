class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == None or len(nums)== 0: return -1
        left, right = 0, len(nums)-1
        while left <= right:
            print("left, mid, right")
            mid = int(left + (right - left) / 2)
            print(left, mid, right)
            print(nums[left], nums[mid], nums[right], "target", target)
            if nums[mid] == target:
                return mid
            elif nums[left] > nums[mid]: #right->sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
            else: #left -> sorted
                if target < nums[mid] and target >= nums[left]:
                    right = mid -1
                else:
                    left = mid + 1
        return -1



if __name__ == '__main__':
    a = Solution()
    sol = a.search([1,2,3,6,5], 6)
    print("solution")        
    print(sol)