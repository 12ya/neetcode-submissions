class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        fresh = time = 0
        
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                cell = grid[r][c]
                if cell == 1:
                    fresh += 1
                if cell == 2 and (r, c):
                    queue.append((r, c))

        while queue and fresh > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited or grid[nr][nc] != 1:
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
        
