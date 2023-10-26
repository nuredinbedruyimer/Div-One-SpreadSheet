from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def goalFind(nums,goal):
            left=0
            right=0
            hashmap=defaultdict(int)
            sum_so_far=0
            ans=0
            while right<len(nums):
                sum_so_far+=nums[right]
                
                if sum_so_far==goal:
                    ans+=1
                if (sum_so_far-goal) in hashmap:
                    ans+=hashmap[sum_so_far-goal]
                
                hashmap[sum_so_far]+=1
              
                right=right+1
            return ans
        return goalFind(nums,goal)
                
                
                    