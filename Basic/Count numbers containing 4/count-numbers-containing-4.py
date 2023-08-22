#User function Template for python3

class Solution:
    def countNumberswith4(self, N):
        count = 0
        for i in range (1,N+1):
            k = str(i)
            for j in k:
                if j == '4':
                    count+=1
                    break
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countNumberswith4(N))
# } Driver Code Ends