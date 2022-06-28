"""
34. 순열 (46) - 343
서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.

Your input
[1,2,3]
Output
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

class Solution:
    """ DFS를 활용한 순열 생성
    dfs를 중첩 함수로 선언하여 인자로 받은 문자열이 없으면 백트래킹을 한다.
    dfs는 인자로 받은 문자열을 반복문을 돌려서, 하나를 제거한 후 dfs를 재귀호출하며, prev_elements는 답을 담는 그릇 역할을 한다.

    이때, 파이썬은 모든 객체를 참조하는 형태로 처리하므로, [:]를 하지 않으면 prev_elements에 대한 참조값이 복사되어 값이 변경될 수 있다. 이 외에도 copy()나 deepcopy()로 처리하는 방법도 있다.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []
        
        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])
                
            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        
        dfs(nums)
        return results