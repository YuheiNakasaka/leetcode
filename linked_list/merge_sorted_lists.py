# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = ListNode(0)
        curr = newList
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            elif l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        curr.next = l1 or l2
        return newList.next

solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

newList = solution.mergeTwoLists(l1, l2)
while newList:
    print(newList.val)
    newList = newList.next