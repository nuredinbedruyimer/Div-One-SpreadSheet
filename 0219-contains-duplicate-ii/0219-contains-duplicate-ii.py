class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter={}
        for index,value in enumerate(nums):
            if (value in counter) and index-counter[value]<=k:
                return True
            else:
                counter[value]=index
        return False
            
            
            
            
            
        