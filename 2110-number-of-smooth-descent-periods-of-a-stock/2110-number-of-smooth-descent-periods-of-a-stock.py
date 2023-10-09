class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        left=0
        counter=0
        for right in range(len(prices)):
            if prices[right-1]-prices[right]!=1:
                left=right
            counter+=right-left+1
        return counter
        