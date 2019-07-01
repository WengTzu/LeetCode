class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        
        #char = set()
        char = dict()
        res = 0
        for right in range(len(s)):
            print(right, s[right])
            if s[right] in char:
                #print("left", left)
                #print("char", char[s[right]])
                left = max(left, char[s[right]] + 1)
                #print("repeat")
            char[s[right]] = right
            res = max(res, right- left +1)
            print(char, res)
        return res
        """while left < len(s) and right < len(s):
            print("before char", char)
            print("left", left, s[left])
            print("right", right, s[right])
            if s[right] in char:
                print("find right in char left + 1")
                if s[left] in char:
                    print("remove")
                    char.remove(s[left])
                left += 1
            else:
                char.add(s[right])
                right += 1
            res = max(res, len(char))
        
            print("after char", char)
            print("res=", res)
            print()
            #print(s)
            #for i, e in enumerate(s):
                #print(i, e)
        return res"""
a = Solution()
sol = a.lengthOfLongestSubstring("abcabcbb")
print("solution")
print(sol)