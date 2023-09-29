class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:

        price.sort()
        # 1 2 5 8 13 21         
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
        left = 0
        right=max(price) - min(price)
        ans = -1
        while left <= right:
            mid = (left + right) //2
            if isTesty(mid,n,counter) >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
        