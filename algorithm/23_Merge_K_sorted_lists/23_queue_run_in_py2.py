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
from queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        """show = [lists[i].val for i in range(len(lists))]
        minVal = min(show)
        print("list", show, minVal)"""
        dummy = ListNode(None)
        curr = dummy

        q = PriorityQueue()

        for node in lists:
            if node:
                print("put", node.val)
                q.put(node.val, node)
        print(q.get())
        
        while not q.empty():
            minNode = q.get()[1]
            curr.next = minNode
            curr = curr.next
            if minNode.next:
                q.put(minNode.next.val, minNode.next)
        curr.next = None
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