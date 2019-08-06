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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or l2 and l1.val > l2.val:
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

node1 = ListNode(1)
node2 = ListNode(1)

node1.next = ListNode(2)
node1.next.next = ListNode(4)
node2.next = ListNode(3)
node2.next.next = ListNode(4)
node2.next.next.next = ListNode(5)

a = Solution()

printNode(node1)
printNode(node2)

sol = a.mergeTwoLists(node1, node2)

print("solution")        
printNode(sol)