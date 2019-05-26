# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        s = 0
        resp = head
        tmp = head
        while tmp:
            s += 1
            tmp = tmp.next
        
        if s == 1:
            resp = None
            return resp
        
        l = s - n
        if n == 1:
          while l >= 0:
              if l == 1:
                  head.next = None
                  break
              head = head.next
              l -= 1
        else:
          while l >= 0:
              if l == 0:
                  head.val = head.next.val
                  head.next = head.next.next
                  break
              head = head.next
              l -= 1
        return resp

# 再帰的な実装
# tailからindex > nになる場所からvalを次のnodeのvalにしていき、
# 最後にnode.nextを返すとうまい具合にnのvalだけ消せる。頭いい。
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         def index(node):
#             if not node:
#                 return 0
#             i = index(node.next) + 1
#             if i > n:
#                 node.next.val = node.val
#             return i
#         index(head)
#         return head.next

list_node = ListNode(1)
list_node.next = ListNode(2)
list_node.next.next = ListNode(3)
list_node.next.next.next = ListNode(4)
list_node.next.next.next.next = ListNode(5)

s = Solution()
nodes = s.removeNthFromEnd(list_node, 2)
while nodes:
    print(nodes.val)
    nodes = nodes.next

list_node = ListNode(1)

s = Solution()
nodes = s.removeNthFromEnd(list_node, 1)
while nodes:
    print(nodes.val)
    nodes = nodes.next

list_node = ListNode(1)
list_node.next = ListNode(2)
s = Solution()
nodes = s.removeNthFromEnd(list_node, 1)
while nodes:
    print(nodes.val)
    nodes = nodes.next