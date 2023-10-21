class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={
            ']':'[',
            '}':'{',
            ')':'(',
        }
        stack=[]
        def isValid(s,hashmap,stack):
            for curr in s:
                if stack and curr in hashmap and  stack[-1]==hashmap[curr]:
                    stack.pop()
                else:
                    stack.append(curr)
            return len(stack)==0
        return isValid(s,hashmap,stack)
                
        