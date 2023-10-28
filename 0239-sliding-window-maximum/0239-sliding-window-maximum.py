class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def Max(nums,k):
            left=0
            right=0
            stack=deque()
            res=[]
            while right<len(nums):
                while  len(stack)>0 and stack[-1]<nums[right]:
                    stack.pop()
                stack.append(nums[right])
                window=right-left+1
                if window<k:
                    right+=1
                elif window==k:
                    res.append(stack[0])
                    if stack[0]==nums[left]:
                        stack.popleft()
                    left+=1
                    right+=1
            return res
        return Max(nums,k)
