class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class circular:
    def __init__(self):
        self.head=None

    def append(self,data):
        if self.head==None:
            self.head=node(data,None)
            self.head.next=self.head
            
        check=self.head
        cur_node=self.head.next
        while(cur_node.next!=check):
            cur_node=cur_node.next
        cur_node.next=node(data,self.head)

    def display(self):
        
        cur_node=self.head.next
        
        
        while(cur_node.next!=self.head):
            print(cur_node.data,end="->")
            cur_node=cur_node.next
        print(cur_node.data,"->",cur_node.next)
        print("address of head is",self.head)
        
    def delete(self,index):
        if index==0:
            cur_node=self.head.next
            while(cur_node.next!=self.head):
                cur_node=cur_node.next
            cur_node.next=self.head.next
            self.head=self.head.next
            return
        cur_node=self.head
        po=0
        while (po<6):
            if po==index:
                cur_node.next=cur_node.next.next
                return
            cur_node=cur_node.next
            po+=1
        




list=circular()
list.append(5)
list.append(6)
list.append(7)
list.append(8)
list.append(9)
list.display()
list.delete(2)

list.display()