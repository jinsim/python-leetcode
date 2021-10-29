# 22) 일일 온도 (P.252) - leetcode(729)
# 매일의 화씨 온도 리스트 T를 입력받아서, 더 따뜻한 날시를 위해서는 며칠을 더 기다려야 하는지를 출력하라

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 더 쉽게 리스트를 생성할 수 있다.
        answer = [0] * len(temperatures)
        stack = []
        # 인덱스와 값이 동시에 필요할 때 유용하다.
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer
