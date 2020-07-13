#leetcode: 44. Wildcard Matching
#nk problem-7
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p)==0:
            return len(s)==0
        elif p[0]=='?':
            return len(s)>0 and self.isMatch(s[1:],p[1:])
        elif p[0]=='*':
            return self.isMatch(s,p[1:]) or len(s)>0 and self.isMatch(s[1:],p)
        else:
            return len(s)>0 and s[0]==p[0] and self.isMatch(s[1:],p[1:])
        
        