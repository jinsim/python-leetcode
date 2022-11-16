""" 58. 리스트 정렬 (489) - 148
연결 리스트를 O(n logn)에 정렬하라.

Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head

        # 런너 기법 활용하여 반을 분할
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None  # 절반 지점에서 노드 간 연결을 끊어주어 반을 분할

        # 분할 재귀호출
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)
