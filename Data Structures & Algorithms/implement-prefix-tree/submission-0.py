class TrieNode:
    def __init__(self, val: str | None, children: dict[str, TrieNode]):
        self.val = val
        self.end = False
        self.children = children

class PrefixTree:
    def __init__(self):
        self.trie = TrieNode(None, {})

    def insert(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char, {})
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
        