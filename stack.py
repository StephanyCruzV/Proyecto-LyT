from dataclasses import dataclass
from operator import truediv

@dataclass
class Stack:
    data: list
    
    def __init__(self):
        self.data = []
    
    def append(self, value):
        if len(self.data) == 0:
            self.data.append(value)
        else:
            top = self.data[-1]

            if top == '(':
                if value == ')':
                    self.data.pop()
                else:
                    self.data.append(value)
            else:
                self.data.append(value)
        
    def pop(self):
        if len(self.data) == 0:
            raise Exception('Trying to pop empty stack')
        else:
            return self.data.pop()
    
    def top(self):
        if len(self.data) == 0:
            raise Exception('Trying to check empty stack')
        else:
            return self.data[-1]

    def empty(self):
        if len(self.data) == 0:
            return True
        elif self.top() == '(':
            return True
        else:
            return False




