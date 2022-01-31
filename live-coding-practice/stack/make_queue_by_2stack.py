class QueueByStack:
    main_arr = []
    sub_arr = []

    def pop(self):
        return self.main_arr.pop()

    def push(self, data):
        if len(self.main_arr) != 0:
            self.make_queue(data)
        else:
            self.main_arr.append(data)

    def make_queue(self, param):
        while self.main_arr:
            data = self.main_arr.pop()
            self.sub_arr.append(data)
        self.main_arr.append(param)
        while self.sub_arr:
            data = self.sub_arr.pop()
            self.main_arr.append(data)

if __name__ == '__main__':
    q = QueueByStack()
    q.push(2)
    q.push(3)
    q.push(4)
    print(q.pop())
    print(q.pop())
    print(q.pop())

