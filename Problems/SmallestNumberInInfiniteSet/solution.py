class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.removed = set()

    def popSmallest(self) -> int:
        output = self.smallest
        self.removed.add(output)
        while self.smallest in self.removed:
            self.smallest += 1
        return output
        

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)