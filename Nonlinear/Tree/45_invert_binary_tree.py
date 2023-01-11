""" 45. 이진 트리 반전(226) - 397
중앙을 기준으로 이진 트리를 반전시키는 문제

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = \
				self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None