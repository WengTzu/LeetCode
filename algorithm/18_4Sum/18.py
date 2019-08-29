import collections
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        dic = collections.defaultdict(set)
        result = set()
        n = len(nums)
        print(dic)
        for i in range(n):
            print("i=",i)
            for j in range(i+1, n):
                print(" j=", j, )
                
                tmp_sum = nums[i] + nums[j]
                print("tmp_sum:", tmp_sum, "<",nums[i], nums[j])

                for half in dic[target - tmp_sum]:
                    print("half", half, "in", dic[target-tmp_sum])
                    print(list(half) + [nums[i] , nums[j]])
                    result.add(tuple(list(half) + [nums[i] , nums[j]]))
                
            for k in range(i):
                print(" k=", k)
                dic[nums[i] + nums[k]].add((nums[k], nums[i]))
            print("dic", dic)
            print("result", result)
        return result
a = Solution()
sol = a.fourSum([1, 0, -1, 0, -2, 2], 0)
#-2, -1, 0, 0, 1, 2
print("solution")
print(sol)