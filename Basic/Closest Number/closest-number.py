#User function Template for python3

class Solution:
    def closestNumber(self, N , M):
        k = N//M
        if k>0:
            a = k*M
            b = (k+1)*M
        else:
            a = (k+1)*M
            b = k*M
        if abs(a-N) == abs(b-M):
            return max(a,b)
        else:
            if abs(a-N)<abs(b-N):
                return a
            else:
                return b


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())
        
        ob = Solution()
        print(ob.closestNumber(N,M))
# } Driver Code Ends