# 14) 두 정렬 리스트의 병합(P.213) - leetcode(21)
# 정렬되어 있는 두 연결 리스트를 합쳐라.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1이 없거나 l2가 존재하고 l1의 값이 l2의 값보다 크다면 스왑한다.
        # 즉, l1에 작은 값을 놔둔다.
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        # l1이 존재한다면, l1의 다음을 재귀적으로 연결한다.
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
