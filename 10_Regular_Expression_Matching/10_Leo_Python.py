"""
s=abcd
p=a*.cd
      S 0 1 2 3
  M   0 1 2 3 4
        a b c d
P 0   T F F F F
0 1 a F F F F F
1 2 * T F F F F
2 3 . F F F F F
3 4 c F F F F F
4 5 d F F F F F

"""
class Solution(object):
    def isMatch(self, s, p):
        x = len(s) + 1
        y = len(p) + 1
        if y == 1: #p=0(p="")
            return x == 1 #x==1 return true else false
        matrix = [[False]*x for i in range(y)]
        matrix[0][0] = True



        for i in range(y-1):
            if p[i] == "*":
                matrix[i + 1][0] = matrix[i - 1][0]
        for i in range(1,y):
            for j in range(1,x):
                if p[i - 1] == ".":
                    matrix[i][j] = matrix[i - 1][j - 1]
                elif p[i - 1] == "*":
                    if p[i - 2] != s[j - 1] and p[i - 2] != ".": #沒批配到
                        matrix[i][j] = matrix[i - 2][j]
                    else:
                        matrix[i][j] = matrix[i - 2][j] or matrix[i - 1][j] or matrix[i][j - 1]
                else:
                     matrix[i][j] = matrix[i - 1][j - 1] and p[i - 1] == s[j - 1]
        #===print===
        """print("s=", end="\t")
        for i in s:
            print(i, end="\t")
        print("\np", end="")
        for i, m in enumerate(matrix):
            for j in m:
                print(j, end="\t")
            if i < y-1:
                print()
                print(p[i], end=">")
        print()"""
        #===print===
        return matrix[-1][-1]
a = Solution()
sol = a.isMatch("aab", "c*a*b*")
print("solution")
print(sol)