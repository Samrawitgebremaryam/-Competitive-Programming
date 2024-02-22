class RecentCounter:

    def __init__(self):
        self.request=deque()

    def ping(self, t: int) -> int:
        self.request.append(t)
        while self.request[0]<t-3000:
            self.request.popleft()
        return len(self.request) 
   
        




    # def __init__(self):
    #     self.request=[]

    # def ping(self, t: int) -> int:
    #     self.request.append(t)
    #     if t<3000:
    #         return len(self.request)
    #     else:
    #         requests.popleft()
    #         if 
            
    #     # return 
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)