class Solution:
    def findMin(self, nums: List[int]) -> int:
        def smallest(arr):
            low = 0
            high = len(arr)-1
            while low < high:
                middle = (low + high)//2
                if arr[middle] <= arr[high]:
                    high = middle
                else:
                    low = middle + 1
            return low
        return nums[smallest( nums)]
                    
        