class node:
    def __init__(self, pre=None, data=None, next=None):
        self.pre = pre
        self.data = data
        self.next = next

class dblinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None  # Added tail reference to track the last node

    def append(self, data):
        if self.head == None:
            self.head = node(None, data, None)
            self.tail = self.head  # The head is also the tail when the list has only one node
        else:
            new_node = node(self.tail, data, None)
            self.tail.next = new_node
            self.tail = new_node  # Move the tail to the newly added node

    def display(self):
        cur_node = self.head
        while cur_node != None:
            print('|', cur_node.data, '|', end=" <-> ")
            cur_node = cur_node.next
        print()
        print("Length:", self.length())

    def length(self):
        co = 0
        cur_node = self.head
        while cur_node != None:
            co += 1
            cur_node = cur_node.next
        return co

    def deleteidx(self, index):
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.pre = None
            else:
                self.tail = None  # If the list is now empty, reset the tail as well
            return
        elif index == (self.length() - 1):
            self.tail = self.tail.pre
            self.tail.next = None
            return

        po = 1
        cur_node = self.head
        while cur_node != None:
            if po == index:
                cur_node.next = cur_node.next.next
                if cur_node.next:
                    cur_node.next.pre = cur_node
                return
            cur_node = cur_node.next
            po += 1

    def printreverse(self):
        cur_node = self.tail  # Start from the tail node (no need to traverse the list)
        while cur_node != None:
            print(cur_node.data, end=" <-> ")
            cur_node = cur_node.pre
        print()

# Example usage
list = dblinkedlist()
list.append(5)
list.append(6)
list.append(7)
list.append(8)
list.printreverse()
list.display()
list.deleteidx(3)
list.display()
