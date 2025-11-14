class CircleQueue:
    '''
    A class to implement a circular queue
    '''
    def __init__(self, size:int):
        self.size = size
        self.queue = [None] * size
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.tail + 1) % self.size == self.head

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.size
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue[self.head]

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue: ", end="")
        for i in range(self.head, self.tail):
            print(self.queue[i], end=" ")
        print()