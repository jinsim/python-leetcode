""" 37. 부분 집합 (78) - 355
모든 부분 집합을 리턴하라.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
class Solution:
    """ 1) 트리의 모든 DFS 결과
    경로 path를 만들어 나가면서 인덱스를 1씩 증가하는 형태로 깊이 탐색한다. 별도의 종료 조건 없이 탐색이 끝나면 저절로 함수가 종료되게 한다.

    부분 집합은 모든 탐색의 경로가 결국 정답이 되므로, 같이 탐색할 때마다 매번 결과를 추가하면 된다.
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(index, path):
            # 매번 결과 추가
            result.append(path)
            
            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        
        dfs(0, [])
        return result