#User function Template for python3

class Solution:
    def getAreas(self, L , W , B , H , R):
        # code here
        a = L*W
        b = int(0.5*B*H)
        c = int(3.14*R*R)
        return a,b,c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        L,W,B,H,R=map(int,input().split())
        
        ob = Solution()
        ptr = ob.getAreas(L,W,B,H,R)
        
        print(ptr[0],ptr[1],ptr[2])
# } Driver Code Ends