class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left=0
        nums.sort()
        for right in range(1,len(nums)):
            if nums[left]==nums[right]:
                return nums[left]
            else:
                left=left+1
        