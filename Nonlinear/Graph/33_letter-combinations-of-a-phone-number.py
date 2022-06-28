"""
32. 섬의 개수 (200) - 331
1을 육지로, 0을 물로 가정한 2D그리드 맵이 주어졌을 때, 섬의 개수를 계산하라.

Your input
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
Output
1
"""

class Solution:
    """ 모든 조합 탐색
    dfs를 중첩 함수로 선언한다. 육지가 아닌 경우에 백트래킹을 하고, 육지를 만나면 0으로 변경한 후, dfs를 각 방향에 맞게 호출한다.

    각 grid 하나하나를 탐색하며 육지인 경우 dfs를 호출하면 된다. 육지로만 구성된 한 덩이가 섬 1개를 나타낸다.
    """
    def letterCombinations(self, digits: str) -> List[str]:
        
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return
            
            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)
        
        # 예외 처리
        if not digits:
            return []
        
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
              "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        result = []
        dfs(0, "")
        
        return result
        