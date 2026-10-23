from collections import defaultdict, deque

class Solution:
    def valid_dist(self, a: str, b: str) -> bool:
        d = 0
        for idx in range(len(a)):
            if d > 1: return False
            if a[idx] != b[idx]: d += 1
        return d == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not (endWord in wordList): return 0

        n = len(wordList)
        graph = defaultdict(list)

        for i in range(n):
            word_a = wordList[i]
            if self.valid_dist(beginWord, word_a):
                graph[beginWord].append(word_a)
            for j in range(i, n):
                word_b = wordList[j]
                if self.valid_dist(word_a, word_b):
                    graph[word_b].append(word_a)
                    graph[word_a].append(word_b)
        
        queue, visited = deque(graph[beginWord]), set()
        t = 1
        while queue:
            t += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord: return t
                visited.add(word)
                for child in graph[word]:
                    if not (child in visited):
                        queue.append(child)
        return 0