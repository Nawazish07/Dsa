class hash:
    def __init__(self,arr=None):
        self.arr=None
        if arr is None:
            self.arr = ["-"] * 6
        else:
            self.arr = arr

    def hashing(self,data):
        
        print(self.arr)
        hash_val = data % len(self.arr)
        
        if self.arr[hash_val] == "-":
            self.arr[hash_val] = data
            
        else:
            k = 0
            while self.arr[hash_val] != "-":
                k += 1
                if k >= len(self.arr):
                    print("no space")
                    return  self.arr
                hash_val = (data % len(self.arr) + k) % len(self.arr)
            self.arr[hash_val] = data
        
    
        print(self.arr,)
        return self.arr
    def find(self,key):
        index=key% len(self.arr)
        if key==self.arr[index]:
            print(key,"Data found at index",index)
        else:
            k=0
            while k <= len(self.arr):
                k += 1
                index = (key % len(self.arr) + k) % len(self.arr)
                if key==self.arr[index]:
                    print(key,"Data found at index",index)
                    return
            print("Search exhausted data didnt exist")
                


h=hash()
h.hashing(1)
h.hashing(11)
h.hashing(12)
h.hashing(13)
h.find(1)
h.find(11)
h.find(16)