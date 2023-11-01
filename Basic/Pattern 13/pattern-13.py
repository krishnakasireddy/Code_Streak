#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        k = (N*(N+1))//2
        l = [0]
        j = 1
        for i in range (1,N+1):
            count = 1
            for j in range (1,k+1):
                if count<=i and j not in l:
                    print(j,end=" ")
                    l.append(j)
                    count+=1
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