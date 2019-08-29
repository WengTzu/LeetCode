# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def printNode(self, node):
        print(node.val, end='')
        if node.next != None:
            self.printNode(node.next)
        else:
            print()
    def addTwoNumbers(self, l1, l2, c=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num = l1.val + l2.val + c
        ret = ListNode(num % 10)
        c = num//10
        print("num", num, "c",c)
        print("l1:",l1.val)
        print("l2:",l2.val)  
        if(l1.next != None or l2.next != None):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        else:
            ret.next = ListNode(c)
        return ret
        #print(l1.next.next.next)

a = Solution()

"""l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next =ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)"""
l1 = ListNode(5)
#l1.next = ListNode(5)
l2 = ListNode(5)
#l2.next = ListNode(5)
#print(l1.val, l1.next.val, l1.next.next.val)
print("l1:")
a.printNode(l1)
print("l2:")
a.printNode(l2)
result = a.addTwoNumbers(l1, l2)
print("result:")
a.printNode(result)
