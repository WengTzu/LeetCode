class Solution(object):
    def intToRoman(self, num):         
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
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        str = ""
        for i in range(0, len(value)):
            while num >= value[i]:
                num -= value[i]
                str += numerals[i]
        return str

a = Solution()
#1~9
sol = a.intToRoman(9)
print("solution")
print(sol)