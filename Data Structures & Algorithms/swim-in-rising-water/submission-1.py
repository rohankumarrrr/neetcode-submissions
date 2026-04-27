import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        visited = set()

        minHeap = [(grid[0][0], 0, 0)] # (maxHeightSeen, row, col)

        STEPS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited.add((0, 0))

        maxHeightSeen = grid[0][0]

        while minHeap:
            minWeight, r, c = heapq.heappop(minHeap)

            if r == N - 1 and c == N - 1:
                return minWeight

            maxHeightSeen = minWeight

            for dr, dc in STEPS:
                nr, nc = r + dr, c + dc
                if (not 0 <= nr < N or
                    not 0 <= nc < N or
                    (nr, nc) in visited):

                    continue
                
                visited.add((nr, nc))

                heapq.heappush(minHeap, (max(maxHeightSeen, grid[nr][nc]), nr, nc))
        
        return maxHeightSeen

        
