# 30) 중복 문자 없는 가장 긴 부분 문자열 (P.303) - leetcode(3)
# 중복 문자가 없는 가장 긴 부분 문자열(substring)의 길이를 리턴하라. 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 해시테이블
        used = {}
        max_length = start = 0
        # s를 enumerate 돌린다.
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면, start의 위치를 갱신한다.
            # 이때 슬라이딩 윈도우 시작점 전에 있는 문자는 used에 있어도 무시해야한다.
            if char in used and start <= used[char]:
                start = used[char] + 1
            # 등장하지 않았던 문자라면 최대 substring 길이를 갱신한다.
            else:
                max_length = max(max_length, index - start + 1)
            # 현재 문자의 위치를 삽입한다.
            used[char] = index
        return max_length
 