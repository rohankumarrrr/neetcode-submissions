class User:
    def __init__(self, userId):
        self.whoUserFollows = set()
        self.userId = userId

class Twitter:
    def __init__(self):
        # stores [userId, tweetId]
        self.tweets = []
        self.users = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not userId in self.users:
            self.users[userId] = User(userId)
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        user = self.users[userId]
        for sourceId, tweetId in self.tweets[::-1]:
            if sourceId in user.whoUserFollows or sourceId == userId:
                res.append(tweetId)
            if len(res) == 10:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self.users:
            self.users[followerId] = User(followerId)
        self.users[followerId].whoUserFollows.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followeeId in self.users[followerId].whoUserFollows:
            return
        self.users[followerId].whoUserFollows.remove(followeeId)
