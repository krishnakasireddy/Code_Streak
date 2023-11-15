#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        
        # code here
        a,b = -1,-1
        for i in range (n):
            if arr[i] == x:
                a = i
                break
        for j in range (n-1,a-1,-1):
            if arr[j] == x:
                b = j
                break
        return a,b

#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends