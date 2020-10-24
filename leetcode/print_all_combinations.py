class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.string = characters
        self.str_length = len(characters)
        self.k = combinationLength
        self.cur_len = -1
        self.bitlist = [0]
        self.combinations = self.get_combinations()

    def bit_count(self,n):
        count = self.bitlist[n//2] + n%2
        self.bitlist.append(count)
        return count

    def get_combinations(self):
        combs = []
        for i in range(1, 1<<self.str_length):
            if self.bit_count(i) == self.k:
                new_combination = ''
                for j in range(self.str_length):
                    if i & (1<<j):
                        new_combination += self.string[j]
                combs.append(new_combination)
        combs.sort()
        return combs

    def next(self) -> str:
        self.cur_len += 1
        return self.combinations[self.cur_len]

    def hasNext(self) -> bool:
        return self.cur_len < len(self.combinations) - 1



# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()