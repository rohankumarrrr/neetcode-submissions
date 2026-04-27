class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        steps = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.appendleft((r, c))
        
        time = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                row, col = q.pop()

                for dr, dc in steps:
                    if (not 0 <= row + dr < ROWS or
                        not 0 <= col + dc < COLS or
                        grid[row + dr][col + dc] != 1):
                    
                        continue

                    grid[row + dr][col + dc] = 2
                    fresh -= 1

                    q.appendleft((row + dr, col + dc))

            time += 1
        
        return time if fresh == 0 else -1