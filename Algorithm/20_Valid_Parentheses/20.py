class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        lookup = {"(" : ")", "{" : "}", "[" : "]"}
        for parenthese in s:
            print(parenthese)
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        if len(stack) == 0:
            return True

                

if __name__ == '__main__':
    a = Solution()
    sol = a.isValid("()[]")
    print("solution")        
    print(sol)