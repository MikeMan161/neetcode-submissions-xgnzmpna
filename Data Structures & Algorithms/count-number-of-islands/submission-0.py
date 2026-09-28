class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def islandSearch(row, col):
            grid[row][col] = "0"
            if (col - 1) >= 0 and grid[row][col - 1] == "1":
                islandSearch(row, col - 1)
            if (col + 1) < len(grid[0]) and grid[row][col + 1] == "1":
                islandSearch(row, col + 1)
            if (row - 1) >= 0 and grid[row - 1][col] == "1":
                islandSearch(row - 1, col)
            if (row + 1) < len(grid) and grid[row + 1][col] == "1":
                islandSearch(row + 1, col)
            return
        col = 0
        row = 0
        numIslands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islandSearch(row, col)
                    numIslands += 1
            col += 1
        row += 1

        return numIslands