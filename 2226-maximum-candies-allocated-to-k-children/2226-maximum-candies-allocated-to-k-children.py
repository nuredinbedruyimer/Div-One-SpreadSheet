class Solution:
    def maximumCandies(self, candies, k):
        n = len(candies)
        left = 1 
        right = max(candies)  
        ans = 0 # 
               

        while left <= right:  # binary search
            numberOfPiles = 0
            mid = (left) + (right - left) // 2

            for i in range(n):   
                numberOfPiles += candies[i] // mid   
            if numberOfPiles >= k: # 
                ans = max(ans, mid)    
                left = mid + 1    
            else: 
                right = mid - 1  
        return ans