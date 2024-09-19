class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        self.head=None

class hashing:
    def __init__(self,arr=None):
        self.arr=None
        if self.arr is None:
            
            self.arr=[node(None,None)]*6
        else:
            self.arr=arr

    def add(self,data):
        
        
        hash_val = data % len(self.arr)
        
        if self.arr[hash_val].data == None:
            self.head=node(data,None)
            self.arr[hash_val] = self.head
            
        else:
            self.head=self.arr[hash_val]
            cur_node=self.head
            while(cur_node.next!=None):
                print(cur_node,end="->")
                cur_node=cur_node.next

            cur_node.next=node(data,None)
        return self.arr
            

    def display(self):
        for i in range(len(self.arr)):
            self.head=self.arr[i]
            cur_node=self.head
            while cur_node!=None:
                print(cur_node.data,end="->")
                cur_node=cur_node.next
            print()
        
    def find(self, key):
        hash_val = key % len(self.arr)  
        cur_node = self.arr[hash_val] 
        
        if cur_node is None:
            print("Data not found")
            return
        
        po = 0 
        while cur_node:
            if key == cur_node.data:
                print("Data found at array index", hash_val, "chained position", po)
                return
            cur_node = cur_node.next 
            po += 1
        
        print("Data not found")


        


h=hashing()
h.add(1)
h.add(7)
h.add(9)
h.display()
h.find(7)