
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data):
        self.items = self.items + [data]

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        data = self.items[0]
        self.items = self.items[1:]
        return data

    def print_queue(self):
        print_str = " ".join(str(item) for item in self.items)
        print(print_str)


if __name__ == "__main__":

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    queue.print_queue() 

    queue.dequeue()
    queue.print_queue()  
