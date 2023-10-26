class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def counterSub(nums):
            left=0
            right=0
            sum_so_far=0
            ans=0
            while right<len(nums):
                sum_so_far+=nums[right]
                
                while left<=right and sum_so_far*(right-left+1)>=k:
                    sum_so_far-=nums[left]
                    left=left+1
                ans+=(right-left+1)
                right=right+1
                
                
            return ans
        return counterSub(nums)
                
                
                
            
        