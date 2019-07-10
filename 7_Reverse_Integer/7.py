class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #print(str(x)[:0:-1])
        if x >= 0:
            x=int(str(x)[::-1])
            #print(x)
        else:
            x = -int(str(x)[:0:-1])
        #print("result:",x)
        #return x
        print(2**31)
        if x > 2147483648 or x < -2147483648:
            return 0
        else:
            return x
        
a = Solution()
sol = a.reverse(1534236469)
print("solution")
print(sol)