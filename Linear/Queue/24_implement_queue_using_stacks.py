# 24) 스택을 이용한 큐 구현 (P.257) - leetcode(232)
# 스택을 이용해 다음 연산을 지원하는 큐를 구현하라.

class MyQueue:

    def __init__(self):
        # 스택 2개를 이용한다.
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        # input 스택에 넣는다.
        self.input.append(x)

    def pop(self) -> int:
        # peek로 반환된 값을 가져온다.
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        # output이 있을 때는 마지막 요소 반환
        # 없을 때는 input에 있는 요소를 output으로 옮겨서 꺼낸다.
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
