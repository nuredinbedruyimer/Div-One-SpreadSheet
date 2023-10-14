#User function Template for python3

class Solution:
    def smallestpositive(self, array, n): 
        array.sort()
        ans=1
        for currIndex in range(n):
            if array[currIndex]>ans:
                break
            else:
                ans=ans+array[currIndex]
        return ans
            
        # Your code goes here  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.smallestpositive(array,n))


# } Driver Code Ends