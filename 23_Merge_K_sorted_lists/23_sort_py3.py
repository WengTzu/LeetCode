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
    def mergeKLists(self, lists):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        num_list = []
        if lists == []:
            return ListNode("")
        else:
            for i in lists:
                while i:
                    num_list.append(i.val)
                    i = i.next
        num_list.sort()
        print(num_list)
        dummy = move = ListNode(0)
        for node in num_list:
            move.next = ListNode(node)
            move = move.next
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
    
    sol = a.mergeKLists([])
    print("solution")        
    printNode(sol)