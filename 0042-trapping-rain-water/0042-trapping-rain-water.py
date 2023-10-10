class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<2:
            return 0
        left=0
        right=len(height)-1
        leftMax=height[left]
        rightMax=height[right]
        counter=0
        while left<right:
            if height[left]>height[right]:
                if height[right]>rightMax:
                    rightMax=height[right]
                else:
                    counter+=rightMax-height[right]
                right=right-1
            else:
                if height[left]>leftMax:
                    leftMax=height[left]
                else:
                    counter+=leftMax-height[left]
                left+=1
        return counter
        