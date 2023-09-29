class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        if k == 0:
            return 0
        price.sort()
        n = len(price)
        counter = 1
        def isTesty(num,n,counter):
            diff = price[0] + num
            for index in range(n):
                if price[index] >= diff:
                    diff = price[index] + num
                    counter += 1
                elif price[index]<diff:
                    continue
            return counter
        low = 0
        high=max(price) - min(price)
        ans = -1
        while low <= high:
            mid = (low + high) //2
            if isTesty(mid,n,counter) >= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
        