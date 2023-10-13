class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex={}
        start=0
        end=0
        ans=[]
        for i,v in enumerate(s):
            lastIndex[v]=i
        for i,v in enumerate(s):
            end=max(end,lastIndex[v])
            start=start+1
            if i==end:
                ans.append(start)
                start=0
        return ans
        