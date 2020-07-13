#leetcode: 241. Different Ways to Add Parentheses
class Solution(object):
    def diffWaysToCompute(self, inp):
        """
        :type input: str
        :rtype: List[int]
        """
        a=[]
        o=[]
        op=['-','+','*']
        n=len(inp)
        i=0
        while i<n:
            num=""
            while i<n and inp[i] not in op:
                num+=inp[i]
                i=i+1
            a.append(int(num))
            if i<n: o.append(inp[i])
            i=i+1
        return self.fun(a,o)        
            
    def fun(self,a,o):
        if len(a)==1:
            return a
        elif len(a)==2:
            if o[0]=='+':return [a[0]+a[1]]
            elif o[0]=='-':return [a[0]-a[1]]
            else:return [a[0]*a[1]]
        else:
            ans=[]
            for i in range(len(o)):
                f=self.fun(a[:i+1],o[:i])
                s=self.fun(a[i+1:],o[i+1:])
                for j in range(len(f)):
                    for k in range(len(s)):
                        ans.append(self.fun([f[j],s[k]],[o[i]])[0])
            return sorted(ans)
                        
                        
                    
            