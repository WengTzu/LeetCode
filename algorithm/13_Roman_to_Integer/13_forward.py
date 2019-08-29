class Solution(object):
    def romanToInt(self, s):         
        """         
        :type num: int         
        :rtype: str    
        Symbol       Value 
        I             1 
        V             5 
        X             10 
        L             50 
        C             100 
        D             500 
        M             1000     
        [1000, 900, 500, 400]
        ['M', 'CM', 'D', 'CD']
        """
        #dict 
        digits = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        for i in range(len(s)):
            if i>0 and digits[s[i]] > digits[s[i-1]]:
                result += digits[s[i]] - 2*digits[s[i-1]]
            else:
                result += digits[s[i]]
        return result
a = Solution()
#1~9
sol = a.romanToInt("MCMXCIV")
print("solution")
print(sol)