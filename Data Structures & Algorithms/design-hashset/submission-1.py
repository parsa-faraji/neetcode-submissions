class MyHashSet:

    def __init__(self):
        self.content = []

    def add(self, key: int) -> None:
        if key not in self.content:
            self.content.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.content)):
            if self.content[i] == key:
                self.content.pop(i)
                return


    def contains(self, key: int) -> bool:
        return key in self.content
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)