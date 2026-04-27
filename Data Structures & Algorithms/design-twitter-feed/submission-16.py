from collections import defaultdict

class Twitter:
    def __init__(self):
        # stores [userId, tweetId]
        self.time = 0
        self.userTweets = defaultdict(list)
        self.whoUsersFollow = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = []
        followees = self.whoUsersFollow[userId]
        followees.add(userId)
        for user in followees:
            candidates.extend(self.userTweets[user])
        heapq.heapify(candidates)
        res = heapq.nsmallest(10, candidates)
        return [tweet for (time, tweet) in res]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.whoUsersFollow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.whoUsersFollow[followerId].discard(followeeId)
