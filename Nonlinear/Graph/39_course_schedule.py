""" 39. 코스 스케쥴(207) - 364
0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0, 1] 쌍으로 표현하는 n개의 코스가 있다.
코스 개수 n과 이 쌍들을 입력으로 받았을 때, 모든 코스가 완료 가능한지 판별하라.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
class Solution:
    """
    이 문제는 그래프가 순환(Cyclic) 구조인지를 판별하는 문제로 풀이할 수 있다. 
    
    먼저 페어들의 목록인 prerequisites 변수를 풀어서 그래프로 표현하고, 페어의 첫번째 값을 x, 두번째 값을 y로 하되, y는 복수개로 구성할 수 있게 한다. 
    
    순환 구조를 찾기 위한 탐색은 dfs()로 진행하며, 순환 구조를 판별하기 위해 이미 방문했던 노드를 traced 변수에 저장한다.  
    현재 노드가 이미 방문했던 노드 집합인 traced에 존재한다면 순환 구조로 간주할 수 있고, 이 경우 False하고 종료할 수 있다. traced는 중복 값을 갖지 않으므로 set() 으로 한다. 
    
    탐색은 재귀로 진행하되, 해당 노드를 이용한 모든 탐색이 끝나게 된다면 traced.remove(i)로 방문했던 내역을 반드시 삭제해야한다. 그렇지 않으면 형제 노드가 방문한 노드까지 남게 되어, 잘못 판단할 수 있기 때문이다.
    """
    def canFinish_1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)
            
        traced = set()
        
        def dfs(i):
            # 순환 구조면 False
            if i in traced:
                return False
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            
            return True
        
        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True
    """ 2) 가지치기를 이용한 최적화
    앞서 DFS 풀이는 순환이 발견될 때까지 모든 자식 노드를 탐색하는 구조로 되어있다.
    
    순환이 아니더라도 복잡하게 서로 호출하는 구조로 그래프가 구성되어 있다면, 풀필요하게 동일한 그래프를 여러번 탐색하게 될 수도 있다. = 한번 방문한 그래프는 다시 방문하지 않도록 무조건 True로 반환하면 탐색 시간을 줄일 수 있다.
    
    원래 DFS는 이런 식으로 가지치기하도록 구현하는 게 올바른 구현 방법이다.
    
    방문한 노드를 저장하기 위해 visited라는 별도의 set() 집합 변수를 만든다. 여기서 visited는 모든 탐색이 끝난 후에 노드를 추가하는 형태로 구현한다. 
    탐색 도중 순환 구조가 발견된다면 False를 리턴하면서 visited 추가는 하지 않음은 물론, 모든 함수를 빠져나가며 종료화게 될 것이다.
    """
    def canFinish_2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)
            
        traced = set()
        visited = set()
        
        def dfs(i):
            # 순환 구조면 False
            if i in traced:
                return False
            # 이미 방문했던 노드면 True
            if i in visited:
                return True
        
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)
            
            return True
        
        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True