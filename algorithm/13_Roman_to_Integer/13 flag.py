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
        use_next = 0
        num = 0

        for i, e in enumerate(s):
            #print(i, e)
            #print(s[i:i+2])
            if use_next == 0:
                if s[i:i+2] in symbols:
                    use_next = 1
                    #i2 = symbols.index(s[i:i+2])
                    num += value[symbols.index(s[i:i+2])]
                else:
                    num += value[symbols.index(s[i])]
            else:
                use_next = 0
            #print("num=", num, use_next)
        return num 


a = Solution()
#1~9
sol = a.romanToInt("IX")
print("solution")
print(sol)