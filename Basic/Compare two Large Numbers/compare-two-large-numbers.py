#User function Template for python3

class Solution:

    def check(self, a,b):
        if a>b:
            return 2
        elif a<b:
            return 1
        else:
            return 3


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        a= int(input())
        b = int(input())

        solObj = Solution()

        print(solObj.check(a,b))
# } Driver Code Ends