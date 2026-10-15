from collections import defaultdict
from heapq import heapify, heappop

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
        heap = [tweet for u in users for tweet in self.posts[u]]
        heapify(heap)

        res = []
        while heap and len(res) < 10:
            res.append(heappop(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
