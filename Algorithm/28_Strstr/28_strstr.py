class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if len(needle) == 0:
            #return 0
        print(len(haystack), len(needle))
        for i in range (len(haystack) - len(needle) + 1):
            print(i)
            #haystack[i: i+len(needle)]
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1
if __name__ == '__main__':
    a = Solution()
    sol = a.strStr(haystack = "hello", needle = "ll")
    print("solution")        
    print(sol)