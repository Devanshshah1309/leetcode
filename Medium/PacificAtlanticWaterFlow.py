class Solution:
    # Create 2 matrice, p_to_a to track which cell can move from pacific -> atlantic and a_to_p for atlantic -> pacific
    # For cell that is already next to pacific, do a DFS and mark all the cell it can reach (the traversal can only continue if there is a larger cell next to the current cell)
    # Do the same thing for cell that is already next to atlantic
    # Find the cells that can be reached from both atlantic and pacific, that is, (i, j) such that both a_to_p[i][j]=1 and p_to_a[i][j]=1
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        res = []
        p_to_a = [[0] * len(heights[0]) for _ in range(len(heights))]
        a_to_p = [[0] * len(heights[0]) for _ in range(len(heights))]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    self.dfs(heights, i, j, p_to_a)
                if i == len(heights)-1 or j == len(heights[0])-1:
                    self.dfs(heights, i, j, a_to_p)
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if p_to_a[i][j] == 1 and a_to_p[i][j] == 1:
                    res.append([i, j])
        
        return res
    
    def dfs(self, heights, i, j, flow):
        if flow[i][j] == 1:
            return
        flow[i][j] = 1
        directions = [(0,1), (0, -1), (1,0), (-1, 0)]
        for choice in directions:
            new_i, new_j = i + choice[0], j + choice[1]
            if (0 <= new_i < len(heights)) and (0 <= new_j < len(heights[0])) and heights[new_i][new_j] >= heights[i][j]:
                self.dfs(heights, new_i, new_j, flow)