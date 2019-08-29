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
        last = 'M'
        num = 0

        for c in s:
            print("Now:",c, "last:", last)
            num += digits[c]

            if digits[last] < digits[c]:
                num -= digits[last]*2
            last = c
            print("num",num)
        return num

a = Solution()
#1~9
sol = a.romanToInt("MCMXCIV")
print("solution")
print(sol)