# 16) 두 수의 덧셈 (P.221) - leetcode(2)
# 역순으로 저장된 연결 리스트의 숫자를 더하라.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 연결 리스트를 뒤집는다.
    # head가 제일 마지막 노드가 된다고 생각. node의 다음을 다음으로 넘기면서, node.next는 이전 노드로 설정한다.
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결 리스트를 파이썬 리스트로 변환한다.
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬 리스트를 연결 리스트로 변환한다.
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    # 두 연결 리스트 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(map(str, a))) + \
            int(''.join(map(str, b)))

        return self.toReversedLinkedList(str(resultStr))
