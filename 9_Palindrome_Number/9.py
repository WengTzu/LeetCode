class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #return str(x) == str(x)[::-1]
        x = str(x)
        y = x[::-1]
        #print("y",y)
        if x == y:
            return True
        else:
            return False
a = Solution()
sol = a.isPalindrome("121")
print("solution")
print(sol)