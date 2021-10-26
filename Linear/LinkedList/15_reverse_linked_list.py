# 15) 역순 연결 리스트 (P.219) - leetcode(206)
# 연결 리스트를 뒤집어라.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 재귀로 풀이
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

    # 반복으로 풀이
    # 재귀보다 반복이 공간, 시간적 측면에서 뛰어나다.
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
