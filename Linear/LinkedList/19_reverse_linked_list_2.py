# 19) 역순 연결 리스트2 (P.237) - leetcode(92)
# 인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 반복 구조로 노드 뒤집기
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 예외 처리
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head
        # start와 end 설정하기
        for _ in range(left - 1):
            start = start.next
        end = start.next

        for _ in range(right-left):
            # 임시 변수를 start의 next로 설정 후, 지금 end 다음에 있는 것을 start도 가리키고, end는 end의 다다음에 있는 것을 가리킨다.
            # 마지막으로 start의 다음이 가리키는 값을 기존 start 다음에 있는 것으로 설정한다.
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next
