class User:
    def __init__(self, userId):
        self.whoUserFollows = set()
        self.userId = userId

from collections import defaultdict

class Twitter:
    def __init__(self):
        # stores [userId, tweetId]
        self.tweets = []
        self.whoUsersFollow = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.whoUsersFollow:
            self.whoUsersFollow[userId] = set()
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        followees = self.whoUsersFollow[userId]
        for sourceId, tweetId in self.tweets[::-1]:
            if sourceId in followees or sourceId == userId:
                res.append(tweetId)
            if len(res) == 10:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.whoUsersFollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followeeId in self.whoUsersFollow[followerId]:
            return
        self.whoUsersFollow[followerId].remove(followeeId)
