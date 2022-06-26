class Solution:
    grid: List[List[str]] # 매개변수에서 제거하기 위해 클래스를 멤버 변수로 선언
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i: int, j: int): # self 제거를 위해 중첩함수로 선언했다.
            # 더 이상 육지가 아닌 경우 종료
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return

            grid[i][j] = '0'

            # 동서남북 탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count