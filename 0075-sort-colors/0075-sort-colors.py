class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left=curr=0
        right=len(nums)-1
        while curr<=right:
            if nums[curr]==2:
                nums[right],nums[curr]=nums[curr],nums[right]
                right=right-1
            elif nums[curr]==0:
                nums[left],nums[curr]=nums[curr],nums[left]
                left+=1
                curr+=1
           
            else:
                curr+=1
        return nums
                
            
            
            
            