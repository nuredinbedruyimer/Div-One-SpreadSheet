class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique = set()
        for i in range(len(nums)):
            if len(unique) >= k+1:
                unique.remove(nums[i-k-1]) # remove left-most elem
            if nums[i] in unique:
                return True
            unique.add(nums[i])
        return False
        
        

            
            
            
            
            
        