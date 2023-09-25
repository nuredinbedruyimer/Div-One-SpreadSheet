class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping={}
        for one in range(len(nums)):
            remain=target-nums[one]
         
            if remain in mapping :
                return [one,mapping[remain]]
            mapping[nums[one]]=one
          
          
    