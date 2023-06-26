from collections import deque

class FrontMiddleBackQueue:
    def __init__(self):
        self.frontDeque = deque()
        self.backDeque = deque()
    
    def pushFront(self, val):
        self.frontDeque.appendleft(val)
        self.balance()
    
    def pushMiddle(self, val):
        if len(self.frontDeque) >= len(self.backDeque):
            self.frontDeque.append(val)
        else:
            self.frontDeque.append(self.backDeque.popleft())
            self.backDeque.appendleft(val)
    
    def pushBack(self, val):
        self.backDeque.append(val)
        self.balance()
    
    def popFront(self):
        if not self.frontDeque and not self.backDeque:
            return -1
        
        if self.frontDeque:
            return self.frontDeque.popleft()
        
        val = self.backDeque.popleft()
        self.balance()
        return val
    
    def popMiddle(self):
        if not self.frontDeque and not self.backDeque:
            return -1
        
        if len(self.frontDeque) == len(self.backDeque):
            return self.frontDeque.pop()
        
        return self.backDeque.popleft()
    
    def popBack(self):
        if not self.frontDeque and not self.backDeque:
            return -1
        
        if self.backDeque:
            return self.backDeque.pop()
        
        val = self.frontDeque.pop()
        self.balance()
        return val
    
    def balance(self):
        if len(self.frontDeque) > len(self.backDeque) + 1:
            self.backDeque.appendleft(self.frontDeque.pop())
        elif len(self.frontDeque) < len(self.backDeque):
            self.frontDeque.append(self.backDeque.popleft())



q = FrontMiddleBackQueue()
q.pushFront(1)
q.pushBack(2)
q.pushMiddle(3)
q.pushMiddle(4)
print(q.popFront())    # Output: 1
print(q.popMiddle())   # Output: 3
print(q.popMiddle())   # Output: 4
print(q.popBack())     # Output: 2
print(q.popFront())    # Output: -1 (The queue is empty)
