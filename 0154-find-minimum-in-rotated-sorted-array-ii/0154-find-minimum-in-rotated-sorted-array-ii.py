class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            while left<right and nums[left]==nums[left+1]:
                left=left+1
            while left<right and nums[right]==nums[right-1]:
                right=right-1
            middle=(left+right)//2
            if nums[middle]<nums[right]:
                right=middle
            else:
                left=middle+1
        return nums[right]
                
            
        