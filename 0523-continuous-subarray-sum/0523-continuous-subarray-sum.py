class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap={0:0}
        currSum=0
        
        #Store The Last Endex of The remainder for element
        for i in range(len(nums)):
            currSum+=nums[i]
           
            if currSum%k not in hashmap:
                hashmap[currSum%k]=i+1
            elif currSum%k in hashmap and hashmap[currSum%k]<i:
                return True
        return False
            
        
        
