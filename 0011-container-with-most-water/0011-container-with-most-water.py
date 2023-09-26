class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maxVolume=0
        while left<right:
            currVolume=(right-left)*min(height[left],height[right])
            maxVolume=max(maxVolume,currVolume)
            if height[left]<height[right]:
                left=left+1
            else:
                right=right-1
        return maxVolume
        