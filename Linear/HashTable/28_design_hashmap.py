# 28) 해시맵 디자인 (P.291) - leetcode(706)
# 다음의 기능을 제공하는 해시맵을 디자인하라. 

class ListNode:
    def __init__(self, key=None, value=None):
        self.key =key
        self.value =value
        self.next = None
        
# 개별 체이닝 방식을 이용한 해시 테이블 구현
class MyHashMap:

    def __init__(self, key=None, value=None):
        self.size = 10000
        self.table = dict()

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료된다. 
        if index not in self.table or self.table[index].value == None:
            self.table[index] = ListNode(key, value)
            return 
        
        # 인덱스에 노드가 존재하는 경우 연결 리스트로 처리한다. 
        p = self.table[index]
        # p가 존재할 때까지 돈다.
        while p:
            if p.key == key:
                p.value=value
                return
            if p.next is None:
                break
            p = p.next
            p.next = ListNode(key, value)
        
        
    def get(self, key: int) -> int:
        index = key % self.size

        if index not in self.table or self.table[index].value == None:
            return -1
        # 노드가 존재할 경우엔 일치하는 키 검색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
        

    def remove(self, key: int) -> None:
        index = key % self.size
        if index not in self.table or self.table[index].value == None:
            return 
        
        # 인덱스의 첫번째 노드일 때 삭제
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return 
        
        # 연결리스트 노드 삭제 
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return 
            prev, p = p, p.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)