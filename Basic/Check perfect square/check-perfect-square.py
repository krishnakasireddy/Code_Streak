#User function Template for python3

#User function Template for python3
import math
class Solution:
    def isPerfectSquare (self, n):
        k = math.sqrt(n)
        a = math.ceil(k)
        b = math.floor(k)
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
        n = int(input())
        
        ob = Solution()
        print(ob.isPerfectSquare(n))
# } Driver Code Ends