class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s == "" or words == []:
            return []
        n = len(words)
        m = len(words[0])
        print(n, m)
        dict = {}
        result = []
        for word in words:
            #(word)
            #print("get", dict.get(word))
            if dict.get(word):
                dict[word] += 1
            else:
                dict.setdefault(word, 1)
        print(dict)
        
        for i in range(len(s) - n * m + 1):
            print(s[i])
            j = i
            k = n
            subdict = dict.copy()
            while k > 0:
                substring = s[j : j+m]
                
                print(substring)
                if subdict.get(substring) == None or subdict[substring] == 0:
                    break
                subdict[substring] -= 1                
                k -= 1
                j += m
                print(substring)
            print("k, i, j")
            print(k, i, j)
            if k == 0:
                result.append(i)
        return result
                

if __name__ == '__main__':
    a = Solution()
    sol = a.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])
    print("solution")        
    print(sol)