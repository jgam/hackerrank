class MyQueue(object):
    def __init__(self):
        self.current_list = []
    
    def peek(self):
        return self.current_list[0]
        
    def pop(self):
        self.current_list.pop(0)
        
    def put(self, value):
        self.current_list.append(value)