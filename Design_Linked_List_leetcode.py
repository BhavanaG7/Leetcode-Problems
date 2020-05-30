class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class MyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def size(self):
        if self.head is None:
            return 0
        temp=self.head
        size=0
        while temp:
            temp=temp.next
            size+=1
        return size
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.head is None:
            return -1

        if index>=self.size():
            return -1
        if index==0:
            return self.head.value
        if index<=self.size()-1 and index>=0:
            count=1
            temp=self.head
            while count<index:
                temp=temp.next
                count+=1
            if count<=index:
                return temp.next.value
            else:
                return -1
        

        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head is None:
            self.head=Node(val)
            return
        new_head=Node(val)
        new_head.next=self.head
        self.head=new_head
        return

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head is None:
            self.head=Node(val)
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=Node(val)
        return
    
    def get_prev_ele(self,pos):
        count=1
        temp=self.head
        while count<pos:
            temp=temp.next
            count+=1
        return temp
    

    
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index==0:
            self.addAtHead(val)
            return
        target=Node(val)
        if self.head is None:
            self.head=target
            target=self.head
            return
        
        prev_node=self.get_prev_ele(index)
        next_node=prev_node.next
        prev_node.next=target
        target.next=next_node
        return

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head == None: 
            return 
        temp = self.head 
        
        if index == 0: 
            self.head = temp.next
            temp = None
            return 

        for i in range(index -1 ): 
            temp = temp.next
            if temp is None: 
                break

        if temp is None: 
            return 
        if temp.next is None: 
            return 
        next = temp.next.next

        temp.next = None

        temp.next = next 
        
    def traverse(self):
        if self.head is None:
            return None
        curr=self.head
        while curr:
            print(curr.value,end=" ")
            curr=curr.next
        return
