class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        result = []
        self.helper(n, n, '', result)
        return result
    
    def helper(self, l, r, item, result):
        if r < l: # ())
            return
        if l > 0:
            self.helper(l-1, r, item+'(', result)
        if r > 0:
            self.helper(l, r-1, item+')', result)
        if l == 0 and r == 0:
            print(item)
            result.append(item)

a = Solution()
sol = a.generateParenthesis(3)
print("solution")        
print(sol)