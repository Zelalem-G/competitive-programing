# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        def bst(node):
            if not node:
                return None
            elif node.val > val:
                return bst(node.left)
            elif node.val < val:
                return bst(node.right)
            else:
                return node
        return bst(root)
        