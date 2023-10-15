#User function Template for python3

class Solution:
    def isStrong(self, N):
        M = N
        fact_sum = 0
        while (M):
            r = M%10
            fact = 1
            for i in range (1,r+1):
                fact*=i
            fact_sum+=fact
            M = M//10
        if N == fact_sum:
            return 1
        else:
            return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isStrong(N))
# } Driver Code Ends