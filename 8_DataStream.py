class DataStream:
    def __init__(self, value, k):
        self.buffer = [-1] * k
        self.value = value
        self.k = k
        self.count = 0
        self.index = 0
    
    def consec(self, num):
        self.count += 1
        self.buffer[self.index] = num
        self.index = (self.index + 1) % self.k
        
        if self.count >= self.k:
            for i in range(self.k):
                if self.buffer[i] != self.value:
                    return False
            return True
        
        return False



dataStream = DataStream(4, 3)
print(dataStream.consec(4))  # Output: False
print(dataStream.consec(4))  # Output: False
print(dataStream.consec(4))  # Output: True
print(dataStream.consec(3))  # Output: False
