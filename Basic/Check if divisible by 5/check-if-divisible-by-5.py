#User function Template for python3
class Solution:
    def divisibleBy5 (ob,N):
        k = N[-1]
        if k == '5' or k == '0':
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=str(input())
       

        ob = Solution()
        print(ob.divisibleBy5(N))
# } Driver Code Ends