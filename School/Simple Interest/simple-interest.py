#User function Template for python3
import math
class Solution:
    def simpleInterest(self,A,B,C):
        #code here
        i = A*B*C
        i/=100
        return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        P,R,T=map(int,input().strip().split(' '))
        ob=Solution()
        print('%.2f'%ob.simpleInterest(P,R,T))
# } Driver Code Ends