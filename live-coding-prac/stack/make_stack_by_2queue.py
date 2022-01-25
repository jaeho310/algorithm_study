class StackByQueue:
    main_queue = []
    sub_queue = []

    def push(self, param):
        if len(self.main_queue) != 0:
            self.make_stack(param)
        self.main_queue.append(param)

    def pop(self):
        return self.main_queue.pop(0)

    def make_stack(self, param):
        while self.main_queue:
            data = self.main_queue.pop(0)
            self.sub_queue.append(data)

        self.main_queue.append(param)

        while self.sub_queue:
            data = self.sub_queue.pop(0)
            self.main_queue.append(data)

if __name__ == '__main__':
    stack = StackByQueue()
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
