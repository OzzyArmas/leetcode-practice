# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # the diameter of a subtree must go up
        def diameter(node) -> (int, int):
            if node is None:
                return (0, -1)
            dl, hl = diameter(node.left)
            dr, hr = diameter(node.right)
        # the comparative is with the height
            return max(hl + 1 + hr + 1, dl, dr), max(hl + 1, hr + 1)
        
        return diameter(root)[0]
