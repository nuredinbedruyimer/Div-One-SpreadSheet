from bisect import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int):
        hi = len(numbers)
        for lo, diff in enumerate(target - num for num in numbers):
            hi = bisect_right(numbers, diff, lo, hi)
 
            if diff == numbers[hi-1]:
                return [lo+1, hi]
                
        