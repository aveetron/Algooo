class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def get_queue(self):
        return self.items



queue = Queue()
queue.enqueue(-100)
queue.enqueue(90)
queue.enqueue(4)
queue.enqueue(55)
queue.enqueue(200)

print(queue.get_queue())
queue.dequeue()
print(queue.get_queue())
print(queue.size())
print(queue.is_empty())