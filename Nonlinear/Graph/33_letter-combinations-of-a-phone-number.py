"""
33. 전화 번호 문자 조합 (17) - 338
2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.

Your input
"23"
Output
["ad","ae","af","bd","be","bf","cd","ce","cf"]

dfs를 중첩 함수로 선언한다. index로 현재 문자열의 길이를 넣고, path로 현재까지의 값을 넣는다.
만약 digits 길이를 넘으면 값을 만족한 것이므로 백트래킹을 한다.

반복문에서는 입력값의 각 인덱스 숫자에 맞춰, 문자를 dfs에 넣는다. 문자열 더하기로 값을 쌓는다.
"""

class Solution:
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
        