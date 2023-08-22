class Solution(object):
    def countNegatives(self, grid):
        ans=0
        for row in grid:
            low=0
            high=len(row)-1
            last=len(row)
            while low<=high:
                middle=(low+high)//2
                if row[middle]>=0:
                    low=middle+1
                else:
                    high=middle-1
            ans+=(last-high-1)
        return ans
            
        