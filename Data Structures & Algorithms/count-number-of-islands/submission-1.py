class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        def dfs(r,c):

            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if grid[r][c] == "0":
                return
            if (r,c) in visited:
                return
            visited.add((r,c))

            directions=[[0,1], [1,0], [-1,0], [0,-1]]
            for dr,dc in directions:
                dfs(r+dr,c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)

        return islands