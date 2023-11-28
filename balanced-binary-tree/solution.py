# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Tuple
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalanceHelper(root) -> Tuple[bool, int]: # must return if balanced and height
            if not root:
                return True, -1
            
            left_bal, left_height = isBalanceHelper(root.left)
            if not left_bal:
                return False, 0
            right_bal, right_height = isBalanceHelper(root.right)
            if not right_bal:
                return False, 0
            return abs(left_height - right_height) < 2, max(left_height, right_height) + 1
        
        return isBalanceHelper(root)[0]
