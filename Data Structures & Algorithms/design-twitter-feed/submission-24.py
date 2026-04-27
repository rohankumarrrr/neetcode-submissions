from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.followMap[userId]
        users.add(userId)
        minHeap = []
        for user in users:
            tweets = self.tweetMap[user]
            for tweet in reversed(tweets[-10:]):
                heapq.heappush(minHeap, tweet)
                if len(minHeap) > 10:
                    heapq.heappop(minHeap)
        return [tweet for _, tweet in heapq.nlargest(10, minHeap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
