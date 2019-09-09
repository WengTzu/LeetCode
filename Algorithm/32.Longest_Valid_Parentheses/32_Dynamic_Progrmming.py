class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        length = len(s)
        dp = [0 for x in range(length)]
        print(s)
        print(dp)

        for i in range(0, length):
            
            print('i=',i, s[i])
            if s[i] == ")":
                j = i -1 - dp[i - 1]
                print(" j=", j)
                if j >= 0 and s[j] == "(":
                    print("   dp[%d] = dp[%d - 1] + 2" % (i, i))
                    dp[i] = dp[i - 1] + 2
                    print("   ", dp)
                    if j - 1 >= 0:
                        print("   dp[%d - 1] = %d" % (i, dp[i-1]))
                        dp[i] += dp[j - 1]            
            print(dp)

if __name__ == '__main__':
    a = Solution()
    sol = a.longestValidParentheses("()())())")
    print("solution")        
    print(sol)