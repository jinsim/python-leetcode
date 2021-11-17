# 23) 큐를 이용한 스택 구현 (P.255) - leetcode(225)
# 큐를 이용해 다음 연산을 지원하는 스택을 구현하라.

class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        # 삽입한 것이 가장 앞에 가도록 한다.(큐는 가장 앞이 먼저 나오므로)
        self.q.append(x)
        # 나머지는 순서대로 넣는다
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # 빼낼 때는 가장 앞에 있는 요소를 가져온다.
        return self.q.popleft()

    def top(self) -> int:
        # 가장 앞 요소 출력
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
