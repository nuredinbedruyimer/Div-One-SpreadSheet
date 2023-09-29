import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def start(nums,targget):
            left=0
            right=len(nums)-1
            ans=-1
            while left<=right:
                middle=(left+right)//2
                if nums[middle]>=target:
                    ans=middle
                    right=right-1
                else:
                    left=left+1
            return ans
        def end(nums,target):
            left=0
            right=len(nums)-1
            ans=-1
            while left<=right:
                middle=(left+right)//2
                if nums[middle]>target:
                    right=middle-1
                else:
                    ans=middle
                    left=left+1
            return ans
        
        print( end(nums,target))
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
            low=start(nums,target)
            high=end(nums,target)
            return [low ,high]
        else:
            return [-1,-1]
        
            
                
        
        

        