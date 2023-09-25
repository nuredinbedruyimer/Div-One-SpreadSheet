class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapping={}
        for one in range(len(numbers)):
            mapping[numbers[one]]=one
        for one in range(len(numbers)):
            remain=target-numbers[one]
            
            if remain in mapping and one !=mapping[remain]:
                return [one+1,mapping[remain]+1]
        