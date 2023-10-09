class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:    
            
        left=0
        right=0
        product=1
        counter=0
        if k<=1:
            return 0
        while right<len(nums):
            product*=nums[right]
            while left<=right and product>=k:
                product/=nums[left]
                left=left+1
            if product<k:
                counter+=(right-left+1)
                right=right+1
        return counter
                
        