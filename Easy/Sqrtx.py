class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = 2**16 
        while low <= high:
            mid = low + (high - low)//2 
			# print(low, mid, high)
            if low == mid:
                if mid*mid == x:
                    return mid
                else:
                    if low*low < x and high*high > x:
                        return low
            if mid*mid < x:
                low = mid + 1 
            elif mid * mid > x:
                high = mid - 1
            else:
                return mid
        return min(low, high)