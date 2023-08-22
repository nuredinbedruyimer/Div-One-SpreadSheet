# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        high=n
        low=1
        while low <=high:
            middle=(low+high)//2
            if guess(middle)==0:
                return middle
            if guess(middle)==-1:
                high=middle-1
            else:
                low=middle+1
        
        