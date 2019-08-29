class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        tips:頭尾不算，來回放入
        """
        if numRows <= 1 or numRows >= len(s):
            return s
        arr = [''] * numRows
        line, step = 0, -1
        for i in s:
            #print("line, step", line, step)
            #print("numRows", numRows)
            #print(i)
            arr[line] += i
            if line % (numRows-1) == 0:
                #print("change way")
                step = -step
            line += step

            #print(arr)
        result = "".join(arr)
        #print(result)
        return result

a = Solution()
sol = a.convert("PAYPALISHIRING", 5)
print("solution")
print(sol)