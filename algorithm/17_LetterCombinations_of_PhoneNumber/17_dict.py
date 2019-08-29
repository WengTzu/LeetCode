class Solution(object):
    def letterCombinations(self, digits):

        number = {
            '2' : 'abc'    ,
            '3' : 'def'    ,
            '4' : 'ghi'    ,
            '5' : 'jkl'    ,
            '6' : 'mno'    ,
            '7' : 'pqrs'   ,
            '8' : 'tuv'    ,
            '9' : 'wxyz'   ,
        }
        if len(digits) == 0:
            return []
        result = [""]
        for i in digits:
            tmp_list = []
            print("digit", i, tmp_list)
            for char in number[i]:
                print("ch", char)
                for str in result:
                    tmp_list.append(str + char)
                print(tmp_list)
            #print(tmp_list)
            result = tmp_list
        return result


a = Solution()
sol = a.letterCombinations("23")
print("solution")
print(sol)