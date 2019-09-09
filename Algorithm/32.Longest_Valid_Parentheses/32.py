class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        just '(' ')'
        """
        stack = []
        result = 0
        start = -1
        for i in range(len(s)):
            print(i, s[i])
            if s[i] == '(':
                stack.append(i)
            else: # s[i] == ')'
                print("len stack", len(stack))
                if len(stack) == 0:
                    start = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        result = max(result, i - start)
                    else:
                        result = max(result, i - stack[-1])
            print("start", start)
            print("stack", stack)
            print("result", result)
        return result
                

if __name__ == '__main__':
    a = Solution()
    sol = a.longestValidParentheses("))))((()((")
    print("solution")        
    print(sol)