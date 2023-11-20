#User function Template for python3

class Solution:
    def printTriangle(self, N):
        for i in range (1,N+1):
            if i%2!=0:
                for j in range (1,i+1):
                    if j%2!=0:
                        print(1,end=" ")
                    else:
                        print(0,end=" ")
                print("")
            else:
                for j in range (1,i+1):
                    if j%2!=0:
                        print(0,end=" ")
                    else:
                        print(1,end=" ")
                print("") 





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends