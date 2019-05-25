# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# ずるい奴
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
#         rev = list(reversed(arr))
#         return True if arr == rev else False

#   1 -> 2 -> 2 -> 1
#   s
#   f
# r

# 1 <- 2 -> 2 -> 1
#      r    s     f

#     1 <- 2 -> 2 -> 1
# r                  f   s
# revを2->1にして、slowも2->1になるLinkedListを作る
# 要素が偶数の場合と奇数の場合があり、奇数の場合はslowを一つずらして調整する
# 最後にrev,slowのvalをそれぞれ比較してNoneまでたどり着けばpalindromeと見なせる
class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev

listNode = ListNode(1)
listNode.next = ListNode(2)
listNode.next.next = ListNode(2)
listNode.next.next.next = ListNode(1)

solution = Solution()
print("Success") if solution.isPalindrome(listNode) else print("Fail")