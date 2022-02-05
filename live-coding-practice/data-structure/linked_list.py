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
        while current:
            print(current.data)
            current = current.next

    def clear(self):
        self.head = None

    def get_index(self, data):
        current = self.head
        cnt = 0
        while current:
            if current.data == data:
                return cnt
            current = current.next
            cnt += 1
        return -1
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(Node(1))
    linked_list.append(Node(2))
    linked_list.print()
    print(linked_list.get_index(2))
