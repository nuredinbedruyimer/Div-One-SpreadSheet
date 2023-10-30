class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        ans=float('inf')
        while left<=right:
            middle=(left+right)//2
            if nums[middle]<nums[right]:
                ans=min(ans,nums[right])
                right=middle
            else:
                ans=min(ans,nums[left])
                left=middle+1
        return ans
                    
        