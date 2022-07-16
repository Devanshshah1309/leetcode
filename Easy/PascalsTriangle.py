class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        ans = [[1], [1,1]]
        for i in range(3, numRows + 1):
            next = [1]
            for j in range(i-2): # number of pairs to add = i - 2
                next.append(ans[-1][j] + ans[-1][j + 1]) # ans[-1] gives the previous row of the triangle
            next.append(1)
            ans.append(next) # no need to do next.copy() because next is a local (loop) variable --> "new" variable every loop anyway (it does not overwrite the previous value of next)
        return ans