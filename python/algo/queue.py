class Queue:
    """Queue implementation"""

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return "The queue is empty"
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        print(len(self.queue))


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()
