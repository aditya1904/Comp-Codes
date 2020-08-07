class WordDictionary:

    class TreeNode:
        def __init__(self):
            self.children = [None for i in range(26)]
            self.eow = False

    def __init__(self):
        self.root = WordDictionary.TreeNode()


    def addWord(self, word: str) -> None:
        current_node = self.root
        for char in word:
            pos = ord(char) - ord('a')
            if(not current_node.children[pos]):
                current_node.children[pos] = WordDictionary.TreeNode()
            current_node = current_node.children[pos]
        current_node.eow = True


    def search(self, word: str) -> bool:
        current_nodes = [self.root]
        for char in word:
            next_ = []
            if char == ".":
                for node in current_nodes:
                    for child in node.children:
                        if(child):
                            next_.append(child)
            else:
                pos = ord(char) - ord('a')
                for node in current_nodes:
                    if(node.children[pos]):
                        next_.append(node.children[pos])
            if not next_:
                return False
            current_nodes = next_
        flag = False
        for node in next_:
            flag = node.eow or flag
        return flag


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)