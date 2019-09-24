class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        sequence = "1"
        for i in range(n-1):
            print("i=%d" %(i))
            print(sequence)
            sequence = self.getNext(sequence)
        return sequence
    def getNext(self, sequence):
        i, next_sequence = 0, ""
        while i < len(sequence):
            count = 1
            while i < len(sequence) - 1 and sequence[i] == sequence[i+1]:
                count += 1
                i += 1
            next_sequence += str(count) + sequence[i]
            i += 1
        return next_sequence 

if __name__ == '__main__':
    a = Solution()
    input = 30
    sol = a.countAndSay(input)
    print("solution")        
    print(sol)