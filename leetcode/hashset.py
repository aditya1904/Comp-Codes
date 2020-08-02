class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hashset = [[[] for i in range(self.size)] for i in range(self.size)]

    def __hashkey(self, num: int) -> int:
        return num % self.size

    def __hashkey2(self, num: int) -> int:
        return num // self.size

    def add(self, key: int) -> None:
        hkey = self.__hashkey(key)
        hkey2 = self.__hashkey2(key)
        self.hashset[hkey][hkey2].append(key)

    def remove(self, key: int) -> None:
        hkey = self.__hashkey(key)
        hkey2 = self.__hashkey2(key)
        if self.contains(key):
            newlist = []
            self.hashset[hkey][hkey2] = newlist


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hkey = self.__hashkey(key)
        hkey2 = self.__hashkey2(key)
        if self.hashset[hkey][hkey2]:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)