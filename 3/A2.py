class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts = {}
        maxlength = 0
        start = 0

        for i, e in enumerate(s):
            print(i, e)
            print(dicts)
            if e in dicts:
                sums = dicts[e] + 1
                print("sums:",sums)
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[e] = i
        return maxlength
        
a = Solution()
sol = a.lengthOfLongestSubstring("abcabcbb")
print("solution")
print(sol)