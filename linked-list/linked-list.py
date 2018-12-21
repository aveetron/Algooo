class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linkedlist(object):

    def __init__(self):
        self.head = Node()

    def append(self,item):
        new_node = Node(item)
        current = self.head
        while current != None:
            current = current.next
        current.next = new_node


    def length(self):
        current = self.head
        total = 0
        while current != None:
            total+=1
            current = current.next
        return total

    def display(self):
        elements = []
        current = self.head
        while current!= None:
            current = current.next
            elements.append(current.next)
        print(elements)

    
linkedlist = Linkedlist()
linkedlist.append(100)
linkedlist.append(-100)
linkedlist.append(500)
linkedlist.display()
print(linkedlist.length())