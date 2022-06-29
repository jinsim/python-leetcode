""" 35. 조합 (77) - 346
전체 수 n을 입력받아 k개의 조합(Combination)을 리턴하라.

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution:
    """
    k개의 조합만을 생성해야한다는 제약 조건이 추가되었고, 조합의 특성 상 본인 이전의 모든 숫자를 제외해야하므로 n과 k를 추가하였다.
    dfs에 k가 0이되면 백트래킹이 되도록 설정하고, 자신 이전의 값은 무시하면서 각 숫자들을 elements에 넣어 재귀 호출하였다.
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return
            
            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
        
        dfs([], 1, k)
        return results