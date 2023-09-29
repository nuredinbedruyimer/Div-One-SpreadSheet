class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left=0
        right=len(nums)-1
        #    [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,|1,1,1,1]|
        '''
        target=2
        left=10
        right=18
        middle=9
        
        
        '''
        while left<right and nums[left]==nums[left+1]:
            left=left+1
        while left<right and nums[right]==nums[right-1]:
            right=right-1
            

     
        while left<=right:
            middle=(left+right)//2
            if nums[middle]==target:
                return True
            elif nums[middle]<nums[right]:
                if nums[middle]<=target and nums[right]>=target:
                    left=middle+1
                else:
                    right=middle-1
            else:
                if nums[left]<=target and  nums[middle]>=target:
                    right=middle-1
                else:
                    left=middle+1
        return False
        