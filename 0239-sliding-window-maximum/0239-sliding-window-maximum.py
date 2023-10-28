class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def Max(nums,k):
            left=0
            right=0
            d=deque()
            res=[]
            while right<len(nums):
                while  len(d)>0 and d[-1]<nums[right]:
                    d.pop()
                d.append(nums[right])
                window=right-left+1
                if window<k:
                    right+=1
                elif window==k:
                    res.append(d[0])
                    if d[0]==nums[left]:
                        d.popleft()
                    left+=1
                    right+=1
            return res
        return Max(nums,k)
