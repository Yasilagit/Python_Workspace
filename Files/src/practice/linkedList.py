class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
            node = Node(data)
            node.next=head
         
    #Complete this method

mylist= Solution()
numberOfElements = int(input)
for i in range(0,numberOfElements,1):
    mylist.insert()