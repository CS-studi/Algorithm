# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        
        return self.check(root.left, root.right)
    
    def check(self, left_node, right_node):
        if left_node is None or right_node is None:
            return left_node == right_node
            
        if left_node.val != right_node.val:
            return False
        
        return self.check(left_node.left, right_node.right) and self.check(left_node.right, right_node.left)