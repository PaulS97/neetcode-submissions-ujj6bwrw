class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        store = {}
        for i, char in enumerate(order):
            store[char] = i
        
        for i in range(0, len(words)-1):
            if not self.compare(words[i], words[i+1], store):
                return False
        return True

    def compare(self, word1, word2, store):
        for i in range(min(len(word1), len(word2))):
            
            if store[word1[i]] == store[word2[i]]:
                continue
            elif store[word1[i]] > store[word2[i]]:
                return False
            else:
                return True

        if len(word2) < len(word1):
            return False

        return True

        