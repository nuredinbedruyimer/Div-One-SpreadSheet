class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        while left<=right:
            middle=(left+right)//2
            if middle*middle==x:
                return middle
            elif middle*middle>x:
                right=middle-1
            else:
                left=middle+1
        return left-1
        