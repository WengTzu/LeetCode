class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a = 0
        print("height", height)
        for i, left in enumerate(height):
            print("i,left",i,left)
            if i < len(height)-1:
            #print(" right:", end=" ")
                for j, right in enumerate(height[i+1:]):
                    print("  ","i,j+1",i, i+j+1, "right", right)
                    #print(right, end=",")
                    w = j+1
                    h = min(left, right)
                    
                    area = w*h
                    a = max(area, a) 
                    print("w,h=", w,h, "max", area)
        return a
a = Solution()
sol = a.maxArea([1,8,6,2,5,4,8,3,7])
print("solution")
print(sol)