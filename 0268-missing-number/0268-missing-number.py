class Solution(object):
    def missingNumber(self, nums):
        n=max(nums)
        arr=[i  for i in range(n+1)]
        def is_Exist(target,arr):
            arr.sort()
            low=0
            high=len(arr)-1
            while low<=high:
                middle=(low+high)//2
                if nums[middle]==target:
                    return True
                if target > nums[middle]:
                    low=middle+1
                else:
                    high=middle-1
            return False
       
                
        for num in arr:
            if is_Exist(num,nums):
                continue
            
            return num 
        return max(arr)+1
            


