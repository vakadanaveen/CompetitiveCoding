#Leetcode: 107. Binary Tree Level Order Traversal II
#Nk trees problem-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        d={}
        level=0
        q=[(root,level)]
        while len(q)>0:
            curr,c_l=q[0]
            if len(q)>1: q=q[1:]
            else: q=[]
            if curr and curr.left: 
                q.append((curr.left,c_l+1))
            if curr and curr.right:
                q.append((curr.right,c_l+1))
            try:
                d[c_l].append(curr.val)
            except Exception:
                d[c_l]=[curr.val]

        m=max(list(d.keys()))
        ans=[]
        for i in range(m,-1,-1):
            ans.append(d[i])
        return ans
            
        