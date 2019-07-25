class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        [""] - indeed have a string ""
        """
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for j in strs[1:]:
                if i >= len(j) or j[i] != strs[0][i]:
                    return strs[0][:i]
                #if i >= len(j):
                #print("compare with", j)
            #print(i, strs[0][i])
        return strs[0]
a = Solution()
sol = a.longestCommonPrefix([""])
print("solution")
print(sol)