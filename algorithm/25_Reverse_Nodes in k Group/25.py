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
    def reverseKGroup(self, head, k):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        curr.next = head
        while curr.next:
            end = curr
            for i in range(k-1):
                end = end.next
                if end.next == None:
                    return dummy.next
            
            curr.next, curr = self.reverse(curr.next, end.next)
        return dummy.next

    def reverse(self, start, end):
        dum = ListNode(0)
        dum.next = start
        while dum.next != end:
            tmp = start.next           
            start.next = tmp.next
            tmp.next = dum.next
            dum.next = tmp
        return end, start
       

if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(4)
    node1.next.next.next.next = ListNode(5)
    node1.next.next.next.next.next = ListNode(6)

    a = Solution()
    
    printNode(node1)
    sol = a.reverseKGroup(node1, 2)
    print("solution")        
    printNode(sol)