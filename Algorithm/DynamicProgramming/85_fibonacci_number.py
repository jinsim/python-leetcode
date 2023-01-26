""" 85. 피보나치 수 (509) - 627
피보나치 수를 구하라.

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""

class Solution:

    #1 재귀 구조 브루트 포스
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
    
    #2 메모이제이션
    dp = collections.defaultdict(int)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]

    #3 타뷸레이션
    dp = collections.defaultdict(int)
    def fib(self, n: int) -> int:
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]

        return self.dp[n]
    #4 두 변수만 이용해 공간 절약
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x+y
        return x
    
    #5 행렬
    def fib(n):
        M = np.matrix([[0, 1], [1, 1]])
        vec = np.array([[0, 1]])

        return np.matmul(M**n, vec)[0]
