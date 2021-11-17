# 29) 보석과 돌 (P.298) - leetcode(771)
# J는 보석이며 S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다. 

import collections

class Solution:
    # 해시 테이블을 이용한 풀이
    def numJewelsInStones1(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0

        # 돌의 빈도 계산
        for i in stones:
            if i not in freqs:
                freqs[i] = 1
            else:
                freqs[i] += 1

        # 보석의 빈도 계산
        for i in jewels:
            if i in freqs:
                count += freqs[i]

        return count
    
    # defaultdict를 이용한 비교 생략 
    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for i in stones:
            freqs[i] += 1

        for i in jewels:
            count += freqs[i]

        return count
    
    # 파이썬다운 방식 
    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
