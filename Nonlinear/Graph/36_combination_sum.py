""" 36. 조합의 합 (39) - 351
숫자 집합 candidates를 조합하여 합이 target이 되는 원소를 나열하라. 각 원소는 중복으로 나열 가능하다.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

합 target을 만들 수 있는 모든 번호 조합을 찾는 문제인데, 앞서 순열과 같이 DFS와 백트래킹으로 풀이할 수 있다. 
순열을 찾는 문제면 자식 노드는 항상 처음부터 시작해야하지만, 조합은 자신부터 하위 원소까지의 나열로만 정리할 수 있다.
"""
class Solution:
    """ 1) DFS로 중복 조합 그래프 탐색
    dfs의 첫번째 파라미터는 합을 갱신해나갈 csum(candidates_sum)이고, 두번째 파라미터는 순서(자기 자신 포함), 세번째 파라미터는 지금까지의 탐색 경로로 정한다.
    
    종료 조건은 csum이 마이너스인 경우(목표값 초과), csum이 0인 경우(target과 일치하는 정답)
    
    dfs()를 호출할 때 i가 아닌 0을 넣으면 된다. 그럼 항상 첫번째 값부터 탐색을 시도하기 때문에 순열로 풀이할 수 있다.
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            
            # 자신부터 하위 원소까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
        
        dfs(target, 0, [])
        return result