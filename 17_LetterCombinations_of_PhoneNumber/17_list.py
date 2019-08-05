class Solution(object):
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        number = ["0","1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = [""]
        """
        for -> digits
        for -> now digits
        for -> result
        """
        #for i in range(len(number)):
            #print(i, number[i])
        for i in digits:
            tmp_list = []
            print("digit", i, tmp_list)
            #print(i, digits[i], number[int(digits[i])])
            for char in number[int(i)]:
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