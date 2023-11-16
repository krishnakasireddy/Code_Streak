#User function Template for python3

class Solution:
    def minValueToBalance(self,a,n):
        #code here.
        k = n//2
        p = sum(a[:k])
        q = sum(a[k:])
        return abs(p-q)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3





t=int(input())
for _ in range(0,t):
    n=int(input())
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.minValueToBalance(a,n)
    print(ans)

# } Driver Code Ends