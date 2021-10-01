class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isLeaf = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.children[ord(ch)-ord('a')]:
                node.children[ord(ch)-ord('a')] = TrieNode()
            node = node.children[ord(ch)-ord('a')]
        node.isLeaf = True
    
    def search(self, word: str, node = None, start = 0) -> bool:
        if node is None:
            node = self.root
        
        for i in range(start, len(word)):
            ch = word[i]
            if ch == '.':
                for child in node.children:
                    if child is not None and self.search(word, child, i+1):
                        return True
                return False
            
            else:
                if not node.children[ord(ch)-ord('a')]:
                    return False
                node = node.children[ord(ch)-ord('a')]
        
        return node.isLeaf
