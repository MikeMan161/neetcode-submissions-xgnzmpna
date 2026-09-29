class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def islandSearch(row, col):
            if row < 0 or row >= len(grid):
                return 0
            elif col < 0 or col >= len(grid[0]):
                return 0
            elif grid[row][col] == 0:
                return 0

            grid[row][col] = 0            
            return (1 + islandSearch(row - 1, col) + islandSearch(row + 1, col) + islandSearch(row, col - 1) + islandSearch(row, col + 1) )

        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    temp = islandSearch(row, col)
                    if temp > maxArea:
                        maxArea = temp
                    temp = 0

        return maxArea