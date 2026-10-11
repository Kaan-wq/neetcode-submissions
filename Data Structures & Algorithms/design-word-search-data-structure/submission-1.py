class TrieNode:
    def __init__(self):
        self.end: bool = False
        self.children: dict[str, TrieNode] = {}

class WordDictionary:
    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True

    def search(self, word: str) -> bool:
        def search_inner(w: str, t: TrieNode) -> bool:
            cur = t
            for i, char in enumerate(w):
                if char == '.':
                    for child in cur.children.values():
                        if search_inner(w[i+1:], child):
                            return True
                    return False
                if char not in cur.children:
                    return False
                cur = cur.children[char]
            return cur.end
        return search_inner(word, self.trie)
