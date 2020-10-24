# def printgrid(grid):
#     for i in range(len(grid)):
#         print(grid[i])

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_oranges = set()
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten_oranges.add((i, j))
        while rotten_oranges:
            new_rotten = set()
            for orange in rotten_oranges:
                x, y = orange[0], orange[1]
                if x >= 0 and x < rows - 1:
                    if grid[x+1][y] == 1:
                        grid[x+1][y] = 2
                        new_rotten.add((x+1, y))
                if x > 0 and x <= rows - 1:
                    if grid[x-1][y] == 1:
                        grid[x-1][y] = 2
                        new_rotten.add((x-1, y))
                if y >= 0 and y < cols - 1:
                    if grid[x][y+1] == 1:
                        grid[x][y+1] = 2
                        new_rotten.add((x, y+1))
                if y > 0 and y <= cols - 1:
                    if grid[x][y-1] == 1:
                        grid[x][y-1] = 2
                        new_rotten.add((x, y-1))
                # printgrid(grid)
            if new_rotten:
                count += 1
            rotten_oranges = new_rotten.copy()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return count
        