#Leetcode: Validate Stack Sequences
#Nk problem-18
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        c=0
        stack=[]
        for x in pushed:
            stack.append(x)
            while stack and c<len(popped) and stack[-1]==popped[c]:
                stack.pop()
                c=c+1
        return c==len(popped)
                
                
            
        