# 17) 페어의 노드 스왑(P.229) - leetcode(24)
# 연결리스트를 입력받아 페어 단위로 스왑하라.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 값만 교환
    def swapPairs1(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head
    """다만, 좋지 않은 피드백을 받을 수 있다. 빠르고 쉬운 풀이를 위해서만이다. """

    # 반복 구조로 스왑
    def swapPairs2(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next
        return root.next

    """그 앞뒤 연결 리스트도 다 수정해야한다. """

    # 재귀 구조로 스왑 (훨씬 더 깔끔)
    def swapPairs3(self, head: ListNode) -> ListNode:
        if head and head.next:
            # head의 다음을 가리키는 포인터 설정
            p = head.next
            # 포인터의 다음으로 재귀 호출, 반환값을 head의 다음으로 잡음.
            # 왜냐하면 head는 앞으로 가서 다음 쌍과 연결될 거기 때문.
            head.next = self.swapPairs3(p.next)
            # 포인터의 다음을 head로 둠. (자리 변경)
            p.next = head
            # 포인터를 반환. (위치가 변경되었으므로)
            return p
        return head
