class TrieNode:
    def __init__(self):
        self.end: bool = False
        self.children: dict[str, TrieNode] = {}

class PrefixTree:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.trie
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
        