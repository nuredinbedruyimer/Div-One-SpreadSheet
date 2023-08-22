class Solution(object):
    def missingNumber(self, nums):
        '''
        [3,0,1]
        [1,2,3]
        diffrence between Them 
        [-2,2,2]
        The Sum Of The Difference become
        total=-2+2+2
        total=2
        as we expect
        other testcase
        [0,1]
        [1,2]
        [1,1]

        
        '''
        target=0
        for i in range(len(nums)):
            target+=(i+1-nums[i])
        return target
            


