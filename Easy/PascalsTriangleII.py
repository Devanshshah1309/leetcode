class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # Observation: You only need the immediately previous row to calculate the next row
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        ans = [1,1]
        for i in range(2, rowIndex + 1):
            next = [1]
            for j in range(i-1): # number of pairs to add = i - 2
                next.append(ans[j] + ans[j + 1])
            next.append(1)
            ans = next # no need to do next.copy() because next is a local (loop) variable --> "new" variable every loop anyway (it does not overwrite the previous value of next)
        return ans