class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #print(strs[0])
        prefix = ""
        result = ""
        prefix_num = 0
        stop = True
        while len(strs)>0:
            result = result + prefix
            for i,c in enumerate(strs):
                if prefix_num >= len(c):
                    return result
                if i == 0:
                    prefix = c[prefix_num]
                if c[prefix_num] != prefix:
                    #print("break")
                    stop = False
                    return result
                #prefix = prefix + c[0]
                #print(c)
            prefix_num += 1
        return result
a = Solution()
sol = a.longestCommonPrefix(["aa","a"])
print("solution")
print(sol)