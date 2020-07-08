#GFG: Stock span problem
#Nk stacks problem-22


#code
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().strip().split(" ")))
    st=[0]
    ans=[1]
    for i in range(1,n):
        st.append(i)
        while len(st)>0 and a[st[-1]]<=a[i]:
            st.pop()
        s = i+1 if len(st)==0 else (i-st[-1])
        ans.append(s)
        st.append(i)
    print(' '.join(map(str,ans)))
    
    