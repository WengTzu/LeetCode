class Solution(object):
    def redivide(self, ldividend, ldivisor):
        print(ldividend, ldivisor)
        if ldividend < ldivisor:
            return 0
        sum, multiple = ldivisor, 1
        while ((sum + sum) >= ldividend):
            sum += sum
            multiple += multiple
        return multiple + self.redivide(ldividend - sum, ldivisor)

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #case 1 + -
        #case 2 overflow
        #case 3 0
            # 3 / 4
            # 0 / 4
        #case 4 normal
        
        #case 1
        sign = 1 # or -1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        print("sign", sign)
        dividend = abs(dividend)
        divisor = abs(divisor)
        #case 2
        if dividend < divisor or divisor == 0:
            return 0
        res = self.redivide(dividend, divisor)
        print(res)

        



        
if __name__ == '__main__':
    a = Solution()
    sol = a.divide(-10, 3)
    print("solution")        
    print(sol)