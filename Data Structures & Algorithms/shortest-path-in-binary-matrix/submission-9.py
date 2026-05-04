class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        ROWS = COLS = len(grid)
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        queue = deque()
        queue.append((0, 0, 1))

        while queue:
            row, col, length = queue.popleft()
            if row == ROWS - 1 and col == COLS - 1:
                return length
            visited.add((row, col))
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 1 or (nr, nc) in visited:
                    continue
                queue.append((nr, nc, length + 1))

        return -1




