class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items = self.items + [data]

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        data = self.items[-1]
        self.items = self.items[:-1]
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.items[-1]

    def print_stack(self):
        print_str = ""
        for item in reversed(self.items):
            print_str += str(item) + " "
        print(print_str.strip())


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()  
    print(stack.pop())  
    stack.print_stack()  
    print(stack.peek()) 
