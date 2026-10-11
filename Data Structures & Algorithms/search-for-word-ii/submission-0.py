class TrieNode:
    def __init__(self):
        self.end: bool = False
        self.children: dict[str, TrieNode] = {}
        self.word = None

class PrefixTree:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str):
        cur = self.trie
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True
        cur.word = word
    
    def search(self, word: str) -> bool:
        cur = self.trie
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = PrefixTree()
        for word in words: 
            tree.insert(word)

        rows, cols = len(board), len(board[0])
        found = []

        def dfs(t: TrieNode, r: int, c: int) -> None:
            if not (0 <= r < rows and 0 <= c < cols): return
            
            char = board[r][c]
            if char not in t.children:
                return

            t = t.children[char]
            if t.word is not None:
                found.append(t.word)
                t.word = None        
            
            board[r][c] = '#'
            dfs(t, r-1, c)
            dfs(t, r, c-1)
            dfs(t, r+1, c)
            dfs(t, r, c+1)
            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(tree.trie, r, c)
        return found
