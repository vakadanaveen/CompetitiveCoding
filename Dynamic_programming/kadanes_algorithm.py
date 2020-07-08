#GFG:Kadane's Algorithm
#Nk: DP problem-6

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().strip().split(" ")))
    m=[0]*n
    for i in range(n):
        if i==0:
            if a[i]>0:
                m[i]=a[i]
                continue
        else:
            if a[i]+m[i-1]>0:
                m[i]=a[i]+m[i-1]
            else:
                m[i]=0
    if max(m)>0: print(max(m))
    else:print(max(a))
            
