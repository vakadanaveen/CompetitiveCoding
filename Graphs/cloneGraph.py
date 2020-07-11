"""
#leetcode 133. Clone Graph
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:return node
        g={}
        q=[node]
        v={}
        while len(q)>0:
            curr=q[0]
            if len(q)==1:q=[]
            else:q=q[1:]
            v[curr.val]=1
            g[curr.val]=[]
            adj1=curr.neighbors
            adj=[]
            for x in adj1:
                if x and x.val not in v.keys():
                    adj.append(x)
            q=q+adj
            for x in adj1:
                if x.val not in g[curr.val]: g[curr.val].append(x.val)
                try:
                    if curr.val not in g[x.val]: g[x.val].append(curr.val)
                except Exception:
                    g[x.val]=[curr.val]
        n_l={}
        for x in g.keys():
            n_l[x]=Node(x,[])
        for x in g.keys():
            for y in g[x]:
                n_l[x].neighbors.append(n_l[y])
        return n_l[1]
            
                    
    
                    
                
        
        