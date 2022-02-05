class Node:
    data = int
    left = None
    right = None

    def __init__(self, data):
        self.data = data


class BinarySearchTree:
    head = Node

    def __init__(self, node):
        self.head = node

    def append(self, node):
        current = self.head
        while True:
            if current.data < node.data:
                if current.left is None:
                    current.left = node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                else:
                    current = current.right

    def is_contain(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            if current.data < data:
                current = current.left
            else:
                current = current.right
        return False



if __name__ == '__main__':
    tree = BinarySearchTree(Node(3))
    tree.append(Node(5))
    tree.append(Node(2))
    tree.append(Node(7))
    tree.append(Node(6))
    print(tree.is_contain(2))
