#GFG: Find length of Loop
#Nk linked list problem-14
#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''

def countNodesinLoop(head):
    #Your code here
    ptr1=ptr2=head
    while ptr1 and ptr2 and ptr2.next and ptr1.next and ptr2.next.next:
        ptr1=ptr1.next
        ptr2=ptr2.next.next
        if ptr1==ptr2:
            break
    else:
        return 0
    
    #Found loop. Find the start node of the loop
    ptr1=head
    while ptr1!=ptr2:
        ptr1=ptr1.next
        ptr2=ptr2.next
    #Find the loop length
    ll=1 #loop length
    ptr2=ptr2.next
    while ptr1!=ptr2:
        ptr2=ptr2.next
        ll=ll+1
    return ll



#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
    
    #connects last node to node at position pos from begining.
    def loopHere(self,pos):
        if pos==0:
            return
        
        walk = self.head
        for i in range(1,pos):
            walk = walk.next
        
        self.tail.next = walk

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))
        
        LL.loopHere(int(input()))
        
        print(countNodesinLoop(LL.head))

# } Driver Code Ends