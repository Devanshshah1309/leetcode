from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # sorted by starting time
        currStart = intervals[0][0]
        currEnd = intervals[0][1]
        result = []
        for interval in intervals:
            if interval[0] <= currEnd:
                currEnd = max(interval[1], currEnd)
            else:
                result.append([currStart, currEnd])
                currStart = interval[0]
                currEnd = interval[1]
        result.append([currStart, currEnd])
        return result