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
from heapq import heappush, heappop, heapreplace, heapify 
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h) #only change heap size when necessary
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next
        return dummy.next

        

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node1.next = ListNode(4)
    node1.next.next = ListNode(5)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)
    node2.next.next.next = ListNode(5)
    node3.next = ListNode(6)

    a = Solution()
    
    printNode(node1)
    printNode(node2)
    printNode(node3)
    
    sol = a.mergeKLists([node1, node2, node3])
    print("solution")        
    #printNode(sol)