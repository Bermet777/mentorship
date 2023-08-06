# creating node
class Node:
    def __init__(self, data, next=None): #constructor
        self.data = data
        self.next = next

# creating linked list
class Linked_list:
    def __init__(self):
        self.head = None

    # insert at the end
    def insert_end(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode        

    # insert at the beginning
    def insert_begin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    # insert between two nodes
    def insert_between(self, middle_node, data):
        newNode = Node(data)
        current = self.head
        while current:
            if current.data == middle_node:
                newNode.next = current.next
                current.next = newNode
                return
            current = current.next
        

    # printing linked list

    def print_ll(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
            

    # deleting an item
    def delete(self, item):
        if self.head is None:
            print('The list is empty.')
            return
        if self.head.data == item:
            self.head = self.head.next
            return

        current = self.head
        previous = None
        while current:
            if current.data == item:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next       

if __name__=='__main__':
    
    LL = Linked_list()
    print('')

    
    LL.insert_end(10)
    LL.insert_end(12)
    LL.insert_end(8)
    LL.insert_end(11)
    LL.insert_end(10)


    # LL.print_ll()
    # LL.delete(12)
    # LL.delete(8)
    # LL.delete(11)
    # LL.print_ll()
    # LL.insert_begin(18)
    # LL.print_ll()
    # LL.insert_between(8, 13)
    # LL.print_ll()

    