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

        """show = [lists[i].val for i in range(len(lists))]
        minVal = min(show)
        print("list", show, minVal)"""
        dummy = ListNode(0)
        curr = dummy
        x = []
        if not lists or not lists[0]:
            return 
        while lists:
            #show each list
            print([lists[i].val for i in range(len(lists))])
            for i in range(len(lists)):
                print("ListNode", i, end=":")
                tmp = lists[i]
                while tmp:
                    print(tmp.val, end='->')
                    tmp = tmp.next
                print()
                #print(lists[0])
            minVal = min([lists[i].val for i in range(len(lists))])
            index = 0

            for l in lists:
                if l.val == minVal:
                    x.append(l)
                    if l.next is None:
                        lists.remove(l)
                    else:
                        lists[index] = l.next
                    break
                index += 1
        for i in range(len(x)-1):
            x[i].next = x[i+1]
            print(x[i].val)
        x[len(x)-1].next = None

        return x[0]
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
    
    sol = a.mergeKLists([[]])
    print("solution")        
    #printNode(sol)