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
        result = ListNode(0)
        now = result
        while l1 and l2:
            print("l1:", end="->")
            printNode(l1)
            print("l2:", end="->")
            printNode(l2)
            if l1.val <= l2.val:
                now.next = l1
                #now.next = l1
                print(l1.val)
                l1 = l1.next
                    
            else:
                now.next = l2
                #now.next = l2
                print(l2.val)
                l2 = l2.next
            now = now.next
        print("end")
        if l1 or l2:
            print("l1", l1)
            print("l2", l2.val)
            now.next = l1 or l2
        return result.next

node1 = ListNode(1)
node2 = ListNode(1)

node1.next = ListNode(2)
node1.next.next = ListNode(4)
node2.next = ListNode(3)
node2.next.next = ListNode(4)
node2.next.next.next = ListNode(5)

a = Solution()
sol = a.mergeTwoLists(node1, node2)
printNode(node1)
printNode(node2)
print("solution")        
printNode(sol)