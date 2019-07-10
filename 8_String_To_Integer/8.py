class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == "":
            return 0

        str = str.strip()

        if str == "":
            return 0
        flag = 1
        
        if str[0] in ['+', '-']:
            if str[0] == '-':
                flag = -1
            str = str[1:]
        #print("after", str)
        num = 0
        if not str[0].isdigit():
            return 0 
        for i in str:
            #print("i=",i)
            if i >= '0' and i <= '9':
                #num = num * 10 + int(i)
                num = num * 10 + ord(i) - ord('0')
                #print("num=",num)
            else:
                break
        num = num*flag
        #print(num)
        #2**31 = 2147483648
        if num > 2147483648-1:
            return 2147483648-1
        elif num < -2147483648:
            return -2147483648
        else:
            return num
        #return 2147483648-1 if x > 2147483648-1 else
a = Solution()
sol = a.myAtoi("3.14159")
print("solution")
print(sol)