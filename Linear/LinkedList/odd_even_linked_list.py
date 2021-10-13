# 18) 홀짝 연결 리스트(P.233) - leetcode(328)
# 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 단, 공간 복잡도 O(1), 시간 복잡도 O(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 반복 구조로 홀짝 처리
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 예외처리
        if head is None:
            return None

        odd = head
        even = head.next
        # 반복이 끝난 후 연결해야하므로
        even_head = head.next

        # 짝수번째가 홀수번째보다 적거나 같으므로
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head
