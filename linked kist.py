class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class Linked_list():
    def __init__(self):
        self.head=None

    def append(self,data):
        
        new_node=node(data, None)
        if self.head is None:
            self.head = new_node
            return
        
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
        cur_node.next=new_node

    def display(self):
        cu_node=self.head
        while cu_node!=None:
            print(cu_node.data, end="-->")
            cu_node = cu_node.next
        print()

    def delete(self,index):
        if index==0:
            self.head=self.head.next
            return
        po=1
        cur_node=self.head
        
        while True:
            pre=cur_node
            cur_node=cur_node.next
            
            if po==index:
                pre.next=cur_node.next
            
                return
            po+=1
    
    def delete_last(self):
        cur_node=self.head
        while(cur_node.next.next!=None):
            
            cur_node=cur_node.next
        cur_node.next=None

    def iat_index(self,index,element):

        if index==0:
            self.head=node(element,self.head)
            return
        cur=1
        cur_node=self.head
        while(cur_node.next!=None):
            if cur==index:
                cur_node.next=node(element,cur_node.next)
            cur+=1
            cur_node=cur_node.next
        


list=Linked_list()
list.append(5)
list.append(6)
list.append(7)
list.append(8)
list.append(9)
list.append(10)
list.display()
list.delete(2)
list.display()
list.delete_last()
list.display()
list.iat_index(index=0,element=4)
list.display()
list.iat_index(index=2,element=4.5)
list.display()