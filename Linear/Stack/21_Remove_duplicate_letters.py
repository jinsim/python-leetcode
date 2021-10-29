# 21) 중복 문자 제거 (P.247) - leetcode(316)
# 중복된 문자를 제외하고 사전식 순서로 나열하라.

# 재귀를 이용한 분리
class Solution:
    def removeDuplicateLetters1(self, s: str) -> str:
        # 집합으로 정렬해서 중복을 제거한다.
        for char in sorted(set(s)):
            # 접미사는 현재 단어 기준으로 뒤쪽의 중복 제거 집합을 의미한다.
            # index와 슬라이싱을 이용해서 쉽게 분리 가능하다.
            suffix = s[s.index(char):]
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행
            if set(s) == set(suffix):
                # 접미사가 없어지면 백트래킹된다.
                # 기준이 된 단어는 뒤 접미사 그룹에서 없앤다.
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

# 스택을 이용한 문제 제거
    def removeDuplicateLetters2(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)
