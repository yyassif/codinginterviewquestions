class MyQueue(object):
    def __init__(self):
        self.front = []
        self.end = []
    
    def peek(self):
        self.process()
        return self.end[-1]
        
    def pop(self):
        self.process()
        return self.end.pop()
        
    def put(self, value):
        self.front.append(value)
    def process(self):
        if not self.end: #end is empty
            while self.front:
                self.end.append(self.front.pop())
queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
