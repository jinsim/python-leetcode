""" 47. 이진 트리 직렬화 & 역직렬화(297) - 406
이진 트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능을 구현하라.

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        queue = collections.deque([root])
        result = ['#']
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    def deserialize(self, data):
        # 예외 처리
        if data == "# #":
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root