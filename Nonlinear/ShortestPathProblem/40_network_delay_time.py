""" 40. 네트워크 딜레이 타임(743) - 375
K부터 출발해 모든 노드가 신호를 받을 수 잇는 시간을 계산하라. 불가능할 경우 -1을 리턴한다. 입력값 u v w는 각각 출발지 도착지 소요시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다.

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
"""

from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # 그래프를 인접 리스트로 생성
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))  # (정점, 걸린시간)

        visited = {}  # 방문한 노드
        Q = [(0, k)]  # 우선순위 큐 (시간, 정점)

        # 우선 순위 큐 최솟값을 기준으로 정점까지의 최단 경로를 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in visited:
                visited[node] = time
                for v, w in graph[node]:
                    heapq.heappush(Q, (time + w, v))

        # 모든 노드의 최단 경로 존재 여부 판별
        if len(visited) == n:
            return max(list(visited.values()))
        return -1  # 신호 받지 못한 노드 존재
