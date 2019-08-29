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
        dummy = jump = ListNode(0)
        dummy.next = head
        l = r = head

        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            
            if count == k:
                cur = l
                pre = r

                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, l = pre, l, r
            else:
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
    sol = a.reverseKGroup(node1, 3)
    print("solution")        
    printNode(sol)