class Solution:
    def maxConsecutiveAnswers(self,answerKey: str, k: int) -> int:
        def Max(answer_key,k):
            counter_false=0
            counter_true=0
            ans=0
            left=0
            right=0
            while right<len(answer_key):
                if answer_key[right]=='F':
                    counter_false+=1
                else:
                    counter_true+=1
                
                while left<=right and min(counter_false,counter_true)>k:
                    if answer_key[left]=='F':
                        counter_false-=1
                    else:
                        counter_true-=1
                    left+=1
                ans=max(ans,right-left+1)
                right=right+1
            return ans
        return Max(answerKey,k)
                        
