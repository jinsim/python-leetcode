""" 38. 일정 재구성(332) - 357
[from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라. 여러 일정이 있는 경우 사전 어휘 순(Lexical Order)으로 방문한다.

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
"""
import collections
class Solution: 
    """ 1) DFS로 일정 그래프 구성
    여행 일정을 그래프로 구성하면 DFS로 풀이할 수 있다. 한가지 주의할 점은, 중복된 일정일 경우 어휘 순으로 방문한다는 점이다. 

    먼저 그래프를 구성하는 작업이 필요하다.
    어휘 순으로 방문해야 하기에, 일단 그래프를 구성한 후에 다시 꺼내 정렬하는 방식을 사용한다.
    
    pop()으로 재귀호출하면서 모두 꺼내 결과에 추가한다. 그래프에서 해당 경로는 사라져서, 재방문하게되지 않을 것이다.
    
    여기서 중요한 점은 어휘 순으로 방문해야한다는 점이다. 어휘순으로 그래프를 생성하기 때문에 pop(0)으로 첫번째 값을 읽어야 한다. 
    마지막에는 다시 뒤집어서 어휘 순으로 맨 처음 읽었던 값이 처음이 되도록 한다.
    """
    def findItinerary_1(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        route = []
        def dfs(a):
            # 첫번째 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
        
        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]
    
    """ 2) 스택 연산으로 큐 연산 최적화 시도
    파이썬 리스트의 경우 pop()은 O(1)이지만 pop(0)은 O(n)이다. 따라서 효율적인 구현을 위해 스택의 연산으로 처리될 수 있도록 개선이 필요하다. 
    
    애당초 그래프를 역순으로 구성하면 추출 시에는 pop()으로 처리가 가능하다.
    이 문제에서는 입력값이 크지 않아서 성능 차이가 거의 없었다.
    """
    def findItinerary_2(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프를 뒤집어서 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
            
        route = []
        def dfs(a):
            # 마지막 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)
        
        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]
    
    """ 3) 일정 그래프 반복
    그래프를 구성하는 부분은 동일하되, 꺼낼 때 재귀가 아닌 스택을 이용한 반복으로 처리한다.

    그래프에 값이 있다면 pop(0)으로 맨 처음 값을 추출하여 스택 변수 stack에 넣게 하고, 그래프의 값을 제거 시켜 while문을 돌리면 순서대로 처리된다.
    
    다만 여행 경로가 끊기는 경우도 있을 것이므로, 재귀와는 다르게 반복에서는 한번 더 풀어내는 변수가 필요하다.
    """
    def findItinerary_3(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route, stack = [], ['JFK']
        while stack:
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]