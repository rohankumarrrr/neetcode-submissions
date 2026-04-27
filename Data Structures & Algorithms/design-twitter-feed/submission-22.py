from collections import defaultdict

class Twitter:
    def __init__(self):
        # stores [userId, tweetId]
        self.time = 0
        self.userTweets = defaultdict(list)
        self.whoUsersFollow = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        followees = self.whoUsersFollow[userId]
        followees.add(userId)
        for user in followees:
            for tweet in reversed(self.userTweets[user][-10:]):
                heapq.heappush(res, tweet)
                if len(res) > 10:
                    heapq.heappop(res) 
        return [tweetId for time, tweetId in heapq.nlargest(10, res)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.whoUsersFollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.whoUsersFollow[followerId].discard(followeeId)
