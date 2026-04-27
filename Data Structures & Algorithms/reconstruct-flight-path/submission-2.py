from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # {"BUF": ["HOU"], "HOU": ["SEA"], "JFK": ["BUF"]}

        # {"HOU": ["JFK"], "SEA": ["JFK"], "JFK": ["HOU", "SEA"]}

        adjList = defaultdict(list)
        for depart, arrive in tickets:
            adjList[depart].append(arrive)
        
        for depart in adjList.keys():
            adjList[depart].sort(reverse=True)

        path = []

        def dfs(depart):
            while adjList[depart]:
                arrive = adjList[depart].pop()
                dfs(arrive)
            path.append(depart)
        
        dfs("JFK")
        
        return path[::-1]

