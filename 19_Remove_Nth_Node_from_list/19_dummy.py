# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def printNode(node):
        print(node.val, end='')
        if node.next != None:
            printNode(node.next)
        else:
            print()
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # s -> dummy
        # f -> dummy
        #dummy -> 1 -> 2 -> 3 -> 4 -> 5
        #           s
        #               f 

        #                   s
        #                             f
        
        result = ListNode(123)
        result.next = head
        s = f = result
        for i in range(n):
            f = f.next
        while f.next:
            
            f = f.next
        s.next = s.next.next
        return result.next
#Node.next.next.next = 

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

a = Solution()
sol = a.removeNthFromEnd(node1, 2)
print(printNode(sol))
print("solution")
#print(sol)