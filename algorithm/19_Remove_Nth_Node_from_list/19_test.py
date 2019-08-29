# Definition for singly-linked list.
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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        deep = 0
        node = head
        while node:
            #print(node.val)
            node = node.next
            deep += 1
        print("deep", deep)
        remove = deep - n
        
        deep = 0
        result = head
        while head:
            current = head

            if deep == remove:
                head = head.next
            deep += 1
            head = head.next
        #result = head
        #printNode(head)
        return result
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
#Node.next.next.next = 
a = Solution()
sol = a.removeNthFromEnd(node1, 2)
print(a.printNode(sol))
print("solution")
#print(sol)