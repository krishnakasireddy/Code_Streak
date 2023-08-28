#User function Template for python3

class Solution:
    def RedOrGreen(self,N,S):
        red,green = 0,0
        for i in S:
            if i == 'R':
                red+=1
            else:
                green+=1
        return min(red,green)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        S=input()
        
        ob=Solution()
        print(ob.RedOrGreen(N,S))
# } Driver Code Ends