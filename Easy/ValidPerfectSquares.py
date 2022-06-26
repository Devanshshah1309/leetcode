class Solution:
	def isPerfectSquare(self, num: int) -> bool:
		low = 0
		high = 2**16 
		while low <= high:
			mid = low + (high - low)//2 
			print(low, mid, high)
			if low == mid:
				if mid*mid == num:
					return True
				else:
					if low*low < num and high*high > num:
						return False
			if mid*mid < num:
				low = mid + 1 
			elif mid * mid > num:
				high = mid - 1
			else:
				return True