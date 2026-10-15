from collections import defaultdict
from heapq import heapify, heappop, heappush

class Twitter:
    def __init__(self):
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.counter, tweetId))
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.follows[userId] | {userId}
        heap = [
            (*self.posts[u][-1], u, len(self.posts[u]) - 1)
            for u in users if self.posts[u]
        ]
        heapify(heap)

        res = []
        while heap and len(res) < 10:
            c, t, u, i = heappop(heap)
            res.append(t)
            if i > 0: heappush(heap, (*self.posts[u][i - 1], u, i - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
