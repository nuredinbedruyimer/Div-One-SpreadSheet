class Solution(object):
    def mySqrt(self, x):
        low=0
        high=x
        while low<=high:
            middle=(high+low)//2
            if middle*middle==x:
                return middle
            elif middle*middle>x:
                high=middle-1
            else:
                low=middle+1
        return low-1
            