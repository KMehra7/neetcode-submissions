# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        #DFS recursively -- Accepted
        # left_h = self.maxDepth(root.left)
        # right_h = self.maxDepth(root.right)
        # return max(left_h, right_h)+1

        #DFS iteratively    
        # stack = [ [root, 1]]
        # levels = 0
        # while stack:
        #     node, level = stack.pop()
        #     if node:
        #         levels = max(levels, level)
        #         stack.append([node.left, level+1])
        #         stack.append([node.right, level+1])
        # return levels

        #BFS
        q = deque([root])
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level
