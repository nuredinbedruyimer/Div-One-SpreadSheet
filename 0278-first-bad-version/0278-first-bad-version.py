# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        low=1
        high=n
       
        while low<=high:
            middle=(low+high)//2
            if  isBadVersion(middle):
               
                high=middle-1
            else:
                low=middle+1
        return low
                
        