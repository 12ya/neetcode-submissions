class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def findPath(r, c, visited):
            ROWS, COLS = len(grid), len(grid[0])
            if (r >= ROWS or c >= COLS) or grid[r][c] == 1 or r < 0 or c < 0 or (r, c) in visited:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            count = 0
            visited.add((r, c))
            count += findPath(r + 1, c, visited)
            count += findPath(r - 1, c, visited)
            count += findPath(r, c + 1, visited)
            count += findPath(r, c - 1, visited)

            visited.remove((r, c))
            return count

        return findPath(0, 0, set())
