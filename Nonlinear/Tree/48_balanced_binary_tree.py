""" 48. 균형 이진 트리(110) - 413
이진 트리가 높이 균형(Height-Balanced) 인지 판단하라.
높이 균형은 모든 노드의 서브 트리 간의 높이 차가 1 이하인 것을 말한다.

Input: root = [3,9,20,null,null,15,7]
Output: true
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)

            # 높이 차가 나는 경우 -1, 이외에는 높이에 따라 1 증가
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return check(root) != -1