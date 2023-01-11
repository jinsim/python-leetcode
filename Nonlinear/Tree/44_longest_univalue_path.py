""" 44. 가장 긴 동일 값의 경로(687) - 393
동일한 값을 지닌 가장 긴 경로를 찾아라.

Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result: int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 합의 최댓값이 결과
            self.result = max(self.result, left+right)

            # 자식 노드 상태값 중 큰 값 반환
            return max(left, right)

        dfs(root)
        return self.result
