class Entry():
    def __init__(self):
        self.children = 26 * [None]
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Entry()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord("a")
            if curr.children[index] is None:
                curr.children[index] = Entry()
            curr = curr.children[index]
        curr.end = True
            

    def search(self, word: str) -> bool:
        return self.search_recur(word, 0, self.root)

    
    def search_recur(self, word, starti, node):
        if node is None:
            return False
        
        if starti == len(word):
            if node.end==True:
                return True
            else:
                return False
        
        if word[starti] == ".":
            for child in node.children:
                if self.search_recur(word, starti+1, child):
                    return True
            return False
        else:
            index = ord(word[starti]) - ord("a")
            return self.search_recur(word, starti+1, node.children[index])
        