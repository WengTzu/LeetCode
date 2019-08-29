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
    def swapPairs(self, head):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        curr.next = head


        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next

            #curr 0, first 1, second 2
            print("cur, fir, second", curr.val, first.val, second.val)
            first.next = second.next
            second.next = first
            curr.next = second
            
            printNode(dummy)
            curr = curr.next.next
            
        return dummy.next


        

        

if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(4)
    node1.next.next.next.next = ListNode(5)
    node1.next.next.next.next.next = ListNode(6)



    a = Solution()
    
    printNode(node1)
    sol = a.swapPairs(node1)
    print("solution")        
    printNode(sol)