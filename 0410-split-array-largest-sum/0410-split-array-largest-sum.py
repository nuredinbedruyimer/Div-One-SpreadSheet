class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def BlackBox(nums,middle,k):
            sum_so_far=0
            counter =0
            for num in nums:
                sum_so_far+=num
                if sum_so_far>middle:
                    sum_so_far=num
                    counter+=1
                    
            return counter+1<=k
                
 
        def splitArrayLargestSum(nums,k):
            low=max(nums)
            high=sum(nums)
            ans=high
            while low<=high:
                middle=(low+high)//2
                if BlackBox(nums,middle,k):
                    ans=middle
                    high=middle-1
                else:
                    low=middle+1
            return ans
        return splitArrayLargestSum(nums,k)
            
        