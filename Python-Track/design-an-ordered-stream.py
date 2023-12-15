class OrderedStream:

    def __init__(self, n: int):
        self.order = [""]*(n+1)
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.order[idKey-1] = value
        arr = []
        
        if idKey-1 == self.pointer:
            while self.order[self.pointer]:
                arr.append(self.order[self.pointer])
                self.pointer+=1
        return arr
         


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)