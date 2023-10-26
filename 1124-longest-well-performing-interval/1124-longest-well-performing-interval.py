class Solution(object):
    def longestWPI(self,hours):
        prefix_sum = [0]
        for hour in hours:
            if hour > 8:
                prefix_sum.append(prefix_sum[-1] + 1)
            else:
                prefix_sum.append(prefix_sum[-1] - 1)

        maxInterval = 0
        seen = {}
        for i in range(len(prefix_sum)):
            if prefix_sum[i] > 0:
                maxInterval = i
            else:
                if prefix_sum[i] not in seen:
                    seen[prefix_sum[i]] = i
                if prefix_sum[i] - 1 in seen:
                    maxInterval = max(maxInterval, i - seen[prefix_sum[i] - 1])

        return maxInterval



