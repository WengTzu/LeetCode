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
        cur_dig = 0
        num = 0

        for i in range(len(s)-1, -1, -1):
            #print(i, s[i], "now",digits[s[i]], "max", cur_dig)
            now = digits[s[i]]
            if now >= cur_dig:
                num += now
                cur_dig = now
            else:
                num -= now
            #print("num",num)
        return num

a = Solution()
#1~9
sol = a.romanToInt("MCMXCIV")
print("solution")
print(sol)