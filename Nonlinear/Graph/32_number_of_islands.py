"""
32. 섬의 개수 (200) - 331
1을 육지로, 0을 물로 가정한 2D그리드 맵이 주어졌을 때, 섬의 개수를 계산하라.

Your input
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
Output
1

dfs를 중첩 함수로 선언한다. 육지가 아닌 경우에 백트래킹을 하고, 육지를 만나면 0으로 변경한 후, dfs를 각 방향에 맞게 호출한다.

각 grid 하나하나를 탐색하며 육지인 경우 dfs를 호출하면 된다. 육지로만 구성된 한 덩이가 섬 1개를 나타낸다.
"""
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