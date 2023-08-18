#User function Template for python3
import math
class Solution:
    def checkPerfectSquare (ob,N):
        k = math.sqrt(N)
        a = math.floor(k)
        b = math.ceil(k)
        if a == b:
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.checkPerfectSquare(N))
# } Driver Code Ends