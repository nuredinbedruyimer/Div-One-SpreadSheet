class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack=[]
        for start in range(len(nums)):
            if len(stack)==0 or nums[stack[-1]]>nums[start]:
                stack.append(start)
        max_width=0
        print(stack)
        for i in range(len(nums)-1,-1,-1):
            
            while stack and nums[stack[-1]]<=nums[i]:
                last=stack.pop()
                max_width=max(max_width,i-last)
                print(max_width)
        return max_width
        
                
        
                
        