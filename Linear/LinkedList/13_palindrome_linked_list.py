# 13) 팰린드롬 연결 리스트(P.201) - leetcode(234)
# 연결 리스트가 팰린드롬 구조인지 판별하라.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 리스트로 변환
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []

        if not head:
            return True
        # 리스트로 변환
        while head:
            stack.append(head.val)
            head = head.next
        # 없을 때 까지 비교
        while len(stack) > 1:
            if stack.pop() != stack.pop(0):
                return False

        return True
    """다만, 속도가 문제다. 동적 배열로 구성된 리스트는 맨 앞 아이템을 가져오기 적합한 자료형이 아니다. 따라서 덱을 사용하는 것이 좋다. 다만 collections 모듈을 주지 않는 코테도 있으므로 생략."""
