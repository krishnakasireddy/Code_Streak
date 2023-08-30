#User function Template for python3


class Solution:
    def findIndex (self,a, N, key ):
        start,end = -1,-1
        for i in range (0,N):
            if a[i] == key:
                start = i
                break
        for i in range (N-1,-1,-1):
            if a[i] == key:
                end = i
                break
        return start,end
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends