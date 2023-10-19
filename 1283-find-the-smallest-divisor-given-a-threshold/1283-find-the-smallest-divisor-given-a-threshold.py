import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def BlackBox(mid,nums,t):
            total=0
            for num in nums:
                total+=math.ceil(num/mid)
            return total<=t
                
        def minDivisor(nums,t):
            low=1
            high=max(nums)
            while low<=high:
                middle=(low+high)//2
                
                if BlackBox(middle,nums,t):
                    ans=middle
                    high=middle-1
                else:
                    low=middle+1
            return ans
        return minDivisor(nums,threshold)
        