class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bitwise = [0] * self.size
        self.reverse = [1] * self.size
        self.count_one = 0
        self.countr=size

    def fix(self, idx: int) -> None:
        if idx < self.size and self.bitwise[idx] == 0:
            self.bitwise[idx] = 1
            self.count_one += 1
            self.countr-=1
            self.reverse[idx] = 0

    def unfix(self, idx: int) -> None:
        if idx < self.size and self.bitwise[idx] == 1:
            self.bitwise[idx] = 0
            self.count_one -= 1
            self.reverse[idx] = 1
            self.countr+=1

    def flip(self) -> None:
        temp = self.bitwise
        self.bitwise = self.reverse
        self.reverse = temp

        tempo = self.count_one
        self.count_one = self.countr
        self.countr = tempo

    def all(self) -> bool:
        return self.count_one == self.size

    def one(self) -> bool:
        return self.count_one != 0

    def count(self) -> int:
        return self.count_one

    def toString(self) -> str:
        new = [str(i) for i in self.bitwise]
        return ''.join(new)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count_ones()
# param_7 = obj.toString()

