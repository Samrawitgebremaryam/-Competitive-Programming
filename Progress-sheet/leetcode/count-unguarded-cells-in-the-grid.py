class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        for i, j in walls:
            grid[i][j] = 3
        for i, j in guards:
            grid[i][j] = 2

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        for x, y in guards:
            for dx, dy in directions:
                a, b = x + dx, y + dy
                while 0 <= a < m and 0 <= b < n and grid[a][b] not in [2, 3]:
                    grid[a][b] = 1
                    a += dx
                    b += dy
        count = 0

        for i in range(m):

            for j in range(n):
                if grid[i][j] == 0:
                    count += 1          
        
        return count
