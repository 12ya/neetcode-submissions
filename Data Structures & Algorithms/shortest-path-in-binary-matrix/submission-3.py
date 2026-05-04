class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = COLS = len(grid)
        visited = set()
        queue = deque()
        queue.append((0, 0, 1))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        if grid[0][0] == 1:
            return -1
            
        while queue:
            row, col, length = queue.popleft()
            if row == ROWS - 1 and col == COLS - 1:
                return length
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 0 or (nr, nc) in visited:
                    continue
                queue.append((nr, nc, length + 1))
                visited.add((nr, nc))
            
        return -1