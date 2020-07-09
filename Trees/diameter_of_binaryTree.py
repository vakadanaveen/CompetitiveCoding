#Leetcode: diameter of a binary tree
#nk trees problem-18
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        l_h=self.height(root.left)
        r_h=self.height(root.right)
        l_d=self.diameterOfBinaryTree(root.left)
        r_d=self.diameterOfBinaryTree(root.right)
        return max(l_h+r_h,max(l_d,r_d))
    def height(self,root):
        if not root:return 0
        return max(self.height(root.left),self.height(root.right))+1
        
        