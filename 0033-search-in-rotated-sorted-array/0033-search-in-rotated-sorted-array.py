class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def rotate_one(arr,target):
            low = 0
            high = len(arr)-1
            while low <= high:
                middle = (low + high)//2
                if arr[middle] == target:
                    return middle
                elif arr[middle] < arr[high]:
                    if arr[middle] < target <= arr[high]:
                        low = middle + 1
                    else:
                        high = middle-1
                else:
                    if arr[low] <= target < arr[middle]:
                        high = middle-1
                    else:
                        low = middle + 1
            return -1
        return rotate_one(nums,target)
        