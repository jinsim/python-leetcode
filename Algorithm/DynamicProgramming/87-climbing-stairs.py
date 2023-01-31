""" 87. 계단 오르기 (70) - 639
당신은 계단을 오르고 있다. 정상에 도달하기 위해 n 계단을 올라야 한다. 매번 각각 1계단 또는 2계단씩 오를 수 있다면, 정상에 도달하기 위한 방법은 몇가지 경로가 되는지 계산하라.

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution:
    #1 재귀 구조 브루트 포스
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    #2 메모이제이션
    dp = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]