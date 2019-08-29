class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #print(str(x)[:0:-1])
        x = int(str(x)[::-1] ) if x >= 0 else -int(str(x)[:0:-1])
        return 0 if x > 2**31 or x <-2**31 else x
        #return x

        
a = Solution()
sol = a.reverse(-123)
print("solution")
print(sol)