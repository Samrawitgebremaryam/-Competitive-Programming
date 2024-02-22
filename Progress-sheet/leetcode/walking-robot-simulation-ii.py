class Robot:

    def __init__(self, width: int, height: int):
        self.width=width
        self.height=height
        self.position=[0,0]
        self.direction="East"

    def step(self, num: int) -> None:
        calculation =(2 * self.width) + (2 * self.height) - 4
        num=num% calculation
        for i in range ( num ):
            if self.position==[0,0]:
                self.direction = "East"
            elif self.position == [self.width - 1,0]:
                self.direction = "North"
            elif self.position == [self.width - 1,self.height - 1]:
                self.direction = "West"
            elif self.position == [0,self.height - 1]:
                self.direction = "South"

            if self.direction == "East":
                self.position[0] += 1
            elif self.direction == "West":
                self.position[0] -= 1
            elif self.direction == "North":
                self.position[1] += 1
            elif self.direction == "South":
                self.position[1] -= 1
        if self.position == [0,0]:
            self.direction = "South"

    def getPos(self) -> List[int]:
        return self.position
        

    def getDir(self) -> str:
        return self.direction
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
