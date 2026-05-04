class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0

        def findIsland(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0' or (nr, nc) in visited:
                        continue
                    
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                cell = grid[r][c]
                if cell == "1" and (r, c) not in visited:
                    findIsland(r, c)
                    islands += 1
        
        return islands