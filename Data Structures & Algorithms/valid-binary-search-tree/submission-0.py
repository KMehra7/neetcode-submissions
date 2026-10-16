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

            return valid(node.left, left_boundary, node.val) and valid(node.right, node.val, right_boundary)

        return valid(root, float("-inf"), float("inf"))


        # if not root: return False
        # parent = root.val
        # left_flag = True if self.isValidBST(root.left) < root.val else False
        # right_flag = True if self.isValidBST(root.right) > root.val else False

        # return left_flag == right_flag