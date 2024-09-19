class node:
    def __init__(self,pre=None,data=None,next=None):
        self.pre=pre
        self.data=data
        self.next=next
    
class dblinkedlist:
    def __init__(self):
        self.head=None

    def append(self,data):
        if self.head==None:
            self.head=node(None,data,None)
            return
        cur_node=self.head
        
        while cur_node.next!=None:
            cur_node=cur_node.next
        new_node=node(cur_node,data,None)
        cur_node.next=new_node
        cur_node=cur_node.next
        return

    def display(self):
        cur_node=self.head
        while cur_node!=None:
            print('|',cur_node.data,'|',end="<->")
            cur_node=cur_node.next
        print()
        print(self.length())
    def length(self):
        co=0
        cur_node=self.head
        while(cur_node!=None):
            co+=1
            cur_node=cur_node.next
        return co

    def deleteidx(self,index):
        if index==0:
            self.head=self.head.next
            self.head.pre=None
            return
        elif index==(self.length()-1):
            
            cur_node=self.head
            while(cur_node.next.next!=None):
                cur_node=cur_node.next
                
            cur_node.next=None
            return

        po=1
        cur_node=self.head
        while cur_node!=None:
            if po==index:
                cur_node.next=cur_node.next.next
                cur_node.next.pre=cur_node

                return
            cur_node=cur_node.next
            po+=1

    




list=dblinkedlist()
list.append(5)
list.append(6)
list.append(7)
list.append(8)

list.display()
list.deleteidx(3)
list.display()
