class Trie:

    class TreeNode:
        def __init__(self):
            self.children = [None for i in range(26)]
            self.eow = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.TreeNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_node = self.root
        for char in word:
            pos = ord(char) - ord('a')
            if(not current_node.children[pos]):
                current_node.children[pos] = Trie.TreeNode()
            current_node = current_node.children[pos]
        current_node.eow = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_node = self.root
        for char in word:
            pos = ord(char) - ord('a')
            if(not current_node.children[pos]):
                return False
            current_node = current_node.children[pos]
        return current_node.eow


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.root
        for char in prefix:
            pos = ord(char) - ord('a')
            if(not current_node.children[pos]):
                return False
            current_node = current_node.children[pos]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)