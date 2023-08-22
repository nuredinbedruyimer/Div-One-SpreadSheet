class Solution(object):
    def isPerfectSquare(self, num):
        low=0
        high=num
        while low<=high:
            middle=(low+high)//2
            if middle*middle==num:
                return True
            if middle*middle>num:
                high=middle-1
            else:
                low=middle+1
        return False
        