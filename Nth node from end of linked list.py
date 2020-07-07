#GFG
#Given a linked list consisting of L nodes and given a number N. The task is to find the Nth node from the end of the linked list

def getNthfromEnd(head,n):
    #code here
    pNthnode=ptemp=head
    i=1
    while ptemp:
        ptemp=ptemp.next
        if i>=n+1:pNthnode=pNthnode.next
        i=i+1
    if i-n>=1:
        return pNthnode.data
    return -1
    
        
