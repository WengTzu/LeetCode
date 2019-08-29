class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        [""] - indeed have a string ""
        """
        result = ""
        i = 0
        while True:
            try:
                sets = set(string[i] for string in strs)
                #print("sets",sets)
                if len(sets) == 1:
                    result += sets.pop()
                    i+=1
                else: break
            except Exception as e:
                break
        return result
            
a = Solution()
sol = a.longestCommonPrefix(["flower","flow","flight"])
print("solution")
print(sol)