class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        self.size += 1

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
        return

    def print(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def get(self, index):
        if index >= self.size:
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current.data


l = List()
l.add(1)
l.add(2)
l.add(3)
l.print()
l.remove(2)
l.print()
print(l.get(1))
