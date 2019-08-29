class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls = len(s)
        lp = len(p)
        print("ls, lp=",ls, lp)
        ls = ls + 1
        lp = lp +1
        #if s == '' or p == ' ': 
            #return False 
        dp = [[False]*lp for i in range(ls)]
        print("array",dp)
        dp[0][0] = True
        for i,c in enumerate(p):
            print("i,c=",i, c,"dp[",0,"][",i-1,"] = ", dp[0][i-1])
            if(c =='*' and dp[0][i-1]):
                print("dp 0", i+1, "=true")
                dp[0][i+1] = True
        print(dp)
        for i,char_s in enumerate(s):
            for j,char_p in enumerate(p):
                print("i,s=",i, char_s, "\tj,p=", j,char_p)
                if char_p == char_s:
                    print("p==s")
                    dp[i+1][j+1] = dp[i][j]
                if char_p == '.':
                    print("p==.")
                    dp[i+1][j+1] = dp[i][j]
                if char_p =='*':
                    if p[j-1] != s[i] and p[j-1] !='.':
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1]  = (dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1])
        print("\t\ts \t0 \t1 \t2 \t3")
        print("p")
        st = "012345"
        for i,e in enumerate(dp):
            if i < 6:
                print(st[i], end="=>")
            for j, e2 in enumerate(e):
                print("\t",e2, end=",")
            print()
        print("dp[",ls-1,"][",lp-1,"] = ",dp[ls-1][lp-1])
        return dp[len(s)][len(p)]
a = Solution()
sol = a.isMatch("abcd", "a*.cd")
print("solution")
print(sol)