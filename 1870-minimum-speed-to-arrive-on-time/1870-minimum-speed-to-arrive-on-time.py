class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def BlackBox(mid, hour, dist):
            meTime = 0
            for i in range(len(dist) - 1):
                meTime += math.ceil(dist[i] / mid)
            meTime += dist[-1] / mid
   
            return meTime <= hour
        def trainSpeed(dist, hours):
            low = 1
            high = 10**8
            ans = -1
            while low <= high:
                middle = (low + high) // 2
                if BlackBox(middle, hours, dist):
                    ans = middle
                    high = middle - 1

                else:
                    low = middle + 1
            return ans


        return trainSpeed(dist, hour)

        