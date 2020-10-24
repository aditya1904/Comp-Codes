class Trie:

    class TreeNode:
        def __init__(self):
            self.children = [None for i in range(26)]
            self.eow = False

    def __init__(self):
        self.root = Trie.TreeNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            pos = ord(char) - ord('a')
            if(not current_node.children[pos]):
                current_node.children[pos] = Trie.TreeNode()
            current_node = current_node.children[pos]
        current_node.eow = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            pos = ord(char) - ord('a')
            if(not current_node.children[pos]):
                return False
            current_node = current_node.children[pos]
        return current_node.eow


    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            pos = ord(char) - ord('a')
            if(not current_node.children[pos]):
                return False
            current_node = current_node.children[pos]
        return True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        sentences = []

        def get_sentences(s, trie):
            start_pos = 0
            for i in range(len(s)):
                if trie.search(s[start_pos:i+1]):
                    word = s[start_pos:i+1] + " "
                    print(word)
                    get_sentences(s[i+1:], trie)

        get_sentences(s, trie)
        return sentences

# ---------------------------------------------------------

class Trie:

    class TreeNode:
        def __init__(self):
            self.children = [None for i in range(26)]
            self.eow = False

    def __init__(self):
        self.root = Trie.TreeNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            pos = ord(char) - ord('a')
            if(not current_node.children[pos]):
                current_node.children[pos] = Trie.TreeNode()
            current_node = current_node.children[pos]
        current_node.eow = True

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            pos = ord(char) - ord('a')
            if(not current_node.children[pos]):
                return False
            current_node = current_node.children[pos]
        return current_node.eow


    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            pos = ord(char) - ord('a')
            if(not current_node.children[pos]):
                return False
            current_node = current_node.children[pos]
        return True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        orig_string = s
        len_s = len(s)
        sentences = []
        sentence = []
        def get_sentences(s, pos, trie, sentence, sentences):
            start_pos = 0
            for i in range(len(s)):
                if trie.search(s[start_pos:i+1]):
                    word = s[start_pos:i+1] + " "
                    sentence.append((pos, pos+i+1, word))
                    if pos+i+1 == len_s:
                        shabds = ''
                        while(len(sentence) > 0):
                            temp = sentence.pop()
                            shabds = temp[2] + " " + shabds
                        sentences.append(shabds)
                    print(pos, pos+i, word)
                    get_sentences(s[i+1:], pos+i+1, trie, sentence, sentences)

        get_sentences(s, 0, trie, sentence, sentences)
        print(sentences)
        return sentences