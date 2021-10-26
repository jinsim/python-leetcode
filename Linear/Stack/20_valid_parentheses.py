# 20) 유효한 괄호 (P.245) - leetcode(20)
# 괄호로 된 입력값이 올바른지 판별하라.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            # table의 키가 아니라면, 여는 괄호이므로 stack에 push한다.
            if char not in table:
                stack.append(char)
            # 닫는 괄호와 만난 상황
            # stack이 비어있거나, 해당 괄호를 여는 것이 최근에 들어온 것이 아니라면 false
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack) == 0
