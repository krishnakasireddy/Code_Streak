#User function Template for python3


class Solution:
    
    def checkIsAP(self, arr, n):
        # code 
        k = sum(arr)
        a = min(arr)
        b = max(arr)
        m = (n*(a+b))//2
        if m == k:
            return True
        else:
            return False
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    # l=list(map(int,input().split()))
    # n=l[0]
    # x=l[1]
    # y=l[2]
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.checkIsAP(a,n)
    if(ans==True):
        print("YES")
    else:
        print("NO")
# } Driver Code Ends