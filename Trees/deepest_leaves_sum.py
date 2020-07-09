#leetcode: 1302. Deepest Leaves Sum
#nk trees problem-12
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        d={}
        level=0
        q=[(root,level)]
        while len(q)>0:
            curr,c_l=q[0]
            if c_l>level:level=c_l
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
        return sum(d[level])
        
        