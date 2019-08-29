class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #if len(height) == 2:
            #return min(height[1],height[0])
        l = 0
        r = len(height)-1
        #print(l,r)
        water = 0
        #for i in height:
        while l<r:
            #print("l, r", l, r)
            area = (r-l)*min(height[l], height[r])
            #print("a=", area)
            water = max(water, area)
            if l == r:
                return water
                break
            elif height[l] < height[r]:
                l += 1
            else:
                r = r-1
a = Solution()
sol = a.maxArea([1,3])
print("solution")
print(sol)