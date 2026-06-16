class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def search(row, col):

            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            search(row+1, col)
            search(row-1, col)
            search(row, col+1)
            search(row, col-1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count +=1
                    search(row, col)
        
        return count