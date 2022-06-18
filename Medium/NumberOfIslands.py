from typing import List

visited = [] # global variable so that I don't need to pass around in methods lol
globalGrid = []
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        global visited, globalGrid
        globalGrid = grid
        visited = [[False for _ in '.'*len(grid[0])] for __ in '.'*len(grid) ]
        count = 0
        # just count the number of times you have to restart bfs
        for row in range(len(visited)):
            for col in range(len(visited[0])):
                if not visited[row][col] and grid[row][col] == "1": # only visited unvisited land.
                    count += 1
                    self.dfs(row, col)
        return count
    
    def dfs(self, row: int, col: int) -> None:
        global globalGrid, visited
        # just set visited[row][col] to true whenever you visit a new cell.
        if row < 0 or col < 0 or row >= len(visited) or col >= len(visited[0]): # out of the grid
            return
        if visited[row][col] or globalGrid[row][col] == "0": # already visited, or water (cannot cross water lmao )
            return
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited[row][col] = True
        for dir in directions:
            self.dfs(row + dir[0], col + dir[1]) # check in all cardinal directions
