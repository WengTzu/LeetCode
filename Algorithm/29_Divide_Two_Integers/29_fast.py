class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        quotient  = 0
        sign = 1

        if divisor < 0:
            divisor = -divisor
            sign = -sign
        if dividend < 0:
            dividend = -dividend
            sign = -sign
        
        print(sign, dividend, divisor)

        while dividend >= divisor:
            
            divisor_tmp = divisor
            j = 1
            dividend -= divisor
            quotient += j
            print(quotient , dividend, divisor)
            while dividend >= divisor_tmp + divisor_tmp:
                j += j
                divisor_tmp += divisor_tmp
                dividend -= divisor_tmp
                quotient += j
                print("  ",quotient , dividend, divisor_tmp)
        print(quotient)
        result = sign * quotient 
        if result > 2**31-1:
            return 2**31-1
        elif result < -2**31:
            return -2**31
        else:
            return result



        
if __name__ == '__main__':
    a = Solution()
    sol = a.divide(-100, 3)
    print("solution")        
    print(sol)