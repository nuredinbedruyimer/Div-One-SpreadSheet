class Solution(object):
    def intersection(self, nums1, nums2):
        set_list_one=set(nums1)
        sorted_list_two=sorted(nums2)
        def is_Exist(target,arr):
            low=0
            high=len(arr)-1
            
            while low<=high:
                middle=(high+low)//2
                if arr[middle]==target:
                    return True
                if target>arr[middle]:
                    low=middle+1
                else:
                    high=middle-1
            return False
        ans=[]
        for num in set_list_one:
            if is_Exist(num,sorted_list_two):
                ans.append(num)
            else:
                continue
        return ans
            
            
        