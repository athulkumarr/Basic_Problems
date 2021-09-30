# This is an implementation of a Trie data structure.
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isLeaf = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def charToIndex(self,ch):
        return ord(ch)-ord('a') 
    
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if node.children[self.charToIndex(ch)] == None:
                node.children[self.charToIndex(ch)] = TrieNode()
            node = node.children[self.charToIndex(ch)]
        node.isLeaf = True    

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if node.children[self.charToIndex(ch)] == None:
                return False
            node = node.children[self.charToIndex(ch)]
        return node.isLeaf

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if node.children[self.charToIndex(ch)] == None:
                return False
            node = node.children[self.charToIndex(ch)]
        return True
