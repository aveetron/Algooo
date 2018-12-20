class Stack(object):

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items


stack = Stack()
stack.push(1)
stack.push(100)
stack.push(500)
stack.push(1000)
print(stack.get_stack())
stack.pop()
print(stack.get_stack())
print(stack.is_empty())