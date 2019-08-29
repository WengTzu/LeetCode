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
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        num = 0
        for i in range(0, len(s)):
            print(s[i], s[i:i+2])
            if s[i:i+2] in symbols and len(s[i:i+2])==2:
                i2 = symbols.index(s[i:i+2])
                num += value[i2]
                i+=1
                print("+",value[i2])
            else:
                print("else")
                print("sym", s[i-1:i+1])
                if s[i-1:i+1] not in symbols or len(s[i-1:i+1]) == 1:
                    i2 = symbols.index(s[i])
                    num += value[i2]
            print("num=", num)
        return num 


a = Solution()
#1~9
sol = a.romanToInt("D")
print("solution")
print(sol)