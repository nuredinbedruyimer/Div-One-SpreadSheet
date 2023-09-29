import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def isFound(nums,target):
            left=0
            right=len(nums)-1
            while left<=right:
                middle=(left+right)//2
                if nums[middle]==target:
                    return True
                elif nums[middle]<target:
                    left=middle+1
                else:
                    right=middle-1
            return False
        if isFound(nums,target):
            low=bisect.bisect_left(nums,target)
            high=bisect.bisect_right(nums,target)
            return [low ,high-1]
        else:
            return [-1,-1]
            
                
        
        

        