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
        items = []
        for user in users:
            for time, tweetId in reversed(self.tweetMap[user][-10:]):
                heapq.heappush(items, (time, tweetId))
                if len(items) > 10:
                    heapq.heappop(items)
        return [tweetId for time, tweetId in heapq.nlargest(10, items)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
