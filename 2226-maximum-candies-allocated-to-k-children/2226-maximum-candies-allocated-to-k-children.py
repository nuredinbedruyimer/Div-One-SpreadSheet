class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canDistribute(candie, k, candies):
            counter = 0
            for c in candies:
                counter += c // candie
            return counter >= k


        def maxCandies(candies, k):
            low = 1
            high = max(candies)
            ans = 0
            while low <= high:
                mid = (low + high) // 2
                if canDistribute(mid, k, candies):
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        return maxCandies(candies,k)
    



        