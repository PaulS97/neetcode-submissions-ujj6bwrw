class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord("a")
            if curr.children[index]==None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            index = ord(char) - ord("a")
            if curr.children[index] is None:
                return False
            else:
                curr = curr.children[index]
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            index = ord(char) - ord("a")
            if curr.children[index] is None:
                return False
            else:
                curr = curr.children[index]
        return True
        
        