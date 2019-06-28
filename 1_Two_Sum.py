class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, e in enumerate(nums):
            print(i, e)
            #print("dict", target-e)
            num = target-e
            print("num=", num)
            if num not in dict:
                print("input dict：", i, e)
                dict[e] = i
            else:
                print("find index")
                #print("num", num)
                print(dict[num], i)
                return dict[num], i
            print("dict", dict)

a = Solution()
sol = a.twoSum([2,7,11,15], 9)
print("solution")
print(sol)
