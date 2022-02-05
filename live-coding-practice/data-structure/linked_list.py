class Node:
    data = ""
    next = None

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    head = None

    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def print(self):
        current = self.head
        res = []
        while current:
            res.append(current.data)
            current = current.next
        print(res)

    def clear(self):
        self.head = None


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(Node(1))
    linked_list.append(Node(2))
    linked_list.print()
