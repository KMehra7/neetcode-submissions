# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        #Global variable, made using self
        self.res = 0

        #USE DFS to return the HEIGHT not DIAMETER
        #Complexity comes from calculating height
        def dfs(curr):
            #Base case for height
            if not curr:
                return 0
            left_h = dfs(curr.left)
            right_h = dfs(curr.right)
            height = max(left_h, right_h) + 1
            #Current diameter is left_h + right_h
            self.res = max(self.res, left_h + right_h)
            return height
        
        dfs(root)
        return self.res        







