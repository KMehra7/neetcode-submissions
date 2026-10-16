# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        #Order is important for below conditions!!
        if not subRoot:
            return True 
        #Since we check subRoot above we only need to check root
        if not root:
            return False

        if self.sameTree(root,subRoot):
            return True
        
        #If root and subRoot are not the same from sameTree function
        #we check the values 
        #Check recursively if the left side or right side of root = subRoot

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    #Use DFS 
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)

        #If one is empty and another isnt simply return False
        return False
