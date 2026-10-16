# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
                
        #since we would pass maxVal till now in our dfs therefor make a new function
        def dfs(node, maxVal):
            if not node: return 0
            #At the root node we ensure res is set to 1
            #thus no need to add separately!!
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            #Computes the result we want
            return res
        #We pass root.val since the root is always a Good Node
        return dfs(root, root.val)

