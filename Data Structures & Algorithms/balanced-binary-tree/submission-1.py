# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #Use Bottom-Up approach
        #go all the way till last node, check if it is balanced or not
        #also get the height of it
        #After calculating for the last node, move up and keep checking
        # Go to right most, then left most, then parent node
        #Traverse like this till you get root node.
        
        def dfs(root):
            if not root:
                return [True, 0]
            #Recursively call left and right nodes
            lefth = dfs(root.left)
            righth = dfs(root.right)

            #balance checks if the entire subtree is balanced at all, not only from the root 
            # balance = lefth[0] and righth[0] and abs( lefth[1] - righth[1] ) <= 1
            if lefth[0] and righth[0] and abs( lefth[1] - righth[1] ) <= 1:
                balance = True
            else:
                balance = False
            #Get height
            height = max(lefth[1], righth[1] ) + 1

            return [balance, height]
        return dfs(root)[0]