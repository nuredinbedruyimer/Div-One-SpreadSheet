class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''2,3,1,2,4,3
                     L
                     R
           Ans=4 4 3 3 2
           Right Move When Ever There is less Sum Than Target value 
           Left Move When we Get Larger Or Equal Sum to that of target
           bacause our target is to find min sub array that equal target
           make sure you return when you get non
        
        '''
        
        
        
        
        def my_func(nums,target):
            left=0
            right=0
            ans=float('inf')
            sum_so_far=0
            while right<len(nums):
                sum_so_far+=nums[right]
                while left<=right and sum_so_far>=target:
                    sum_so_far-=nums[left]
                    
                    ans=min(ans,right-left+1)
                    left=left+1
                right=right+1
            if ans==float('inf'):
                return 0
            else:
                return ans
        return my_func(nums,target)
                
                     
        