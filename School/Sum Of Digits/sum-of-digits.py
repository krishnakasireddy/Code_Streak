#User function Template for python3

class Solution:
    def sumOfDigits (self, N):
        num_sum = 0
        while (N):
            rem = N%10
            num_sum+=rem
            N = N//10
        return num_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.sumOfDigits(N))
# } Driver Code Ends