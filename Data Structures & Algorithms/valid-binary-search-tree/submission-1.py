# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #We will do inorder traversal
        #that we can compute left node value first, then root and compare
        #then we'll have root value and then check with right node

        #Pass boundaries; update them for left and right subtrees resp.
        def valid(node, left_boundary, right_boundary):
            if not node: return True #Since empty BST is a valid BST
            if not (left_boundary < node.val < right_boundary): return False
            #Update right boundary for left subtree and left boundary for right subtree
            #If we get a node inside for whom both boundaries need to be updated
            #Then we would be able to check the tree's validity using both boundaries
            return valid(node.left, left_boundary, node.val) and valid(node.right, node.val, right_boundary)

        return valid(root, float("-inf"), float("inf"))


        # if not root: return False
        # parent = root.val
        # left_flag = True if self.isValidBST(root.left) < root.val else False
        # right_flag = True if self.isValidBST(root.right) > root.val else False

        # return left_flag == right_flag