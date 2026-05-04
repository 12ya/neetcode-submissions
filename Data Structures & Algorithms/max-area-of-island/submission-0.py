class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c) -> int:
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            area = 1

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited or grid[nr][nc] != 1:
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    area += 1
            return area

        
        for r in range(ROWS):
            for c in range(COLS):
                cell = grid[r][c]
                if cell == 1 and (r, c) not in visited:
                    maxArea = max(bfs(r, c), maxArea)

        return maxArea
