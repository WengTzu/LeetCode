class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        quotient = 0
        if dividend == 0:
            return 0
        elif divisor == 1:
            quotient =  dividend
        elif divisor == -1:
            quotient = -dividend
        elif dividend < 0 and divisor < 0:
            print('case 1')
            while dividend - divisor <= 0:
                dividend -= divisor
                quotient += 1
        elif dividend < 0 and divisor > 0:
            print('case 2')
            while dividend + divisor <= 0:
                dividend += divisor
                quotient -= 1
        elif dividend > 0 and divisor > 0:
            print('case 3')
            while dividend - divisor >= 0:
                dividend -= divisor
                quotient += 1
        else:
            print('case 4')
            while dividend + divisor >= 0:
                dividend += divisor
                quotient -= 1
        if quotient >= 2147483648:
            quotient -= 1
        elif quotient <= -2147483648:
            quotient += 1
        return quotient
        
if __name__ == '__main__':
    a = Solution()
    sol = a.divide(-2147483648, -1)
    print("solution")        
    print(sol)