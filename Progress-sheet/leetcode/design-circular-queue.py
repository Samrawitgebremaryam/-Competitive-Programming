class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=[0]*k
        self.queuesize=0
        self.rear=-1 
        self.k = k      
        self.front=0
        
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear+=1
            self.queue[self.rear % self.k]=value
            self.queuesize+=1
            return True 
        return False 

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False 
        self.front+=1
        self.queuesize-=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1 
        return self.queue[self.front % self.k] 
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1 
        return self.queue[self.rear % self.k] 
        # return self.queue[(self.rear ) % self.k]

            
    def isEmpty(self) -> bool:
        return self.queuesize==0
        

    def isFull(self) -> bool:
        return self.queuesize==len(self.queue)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()