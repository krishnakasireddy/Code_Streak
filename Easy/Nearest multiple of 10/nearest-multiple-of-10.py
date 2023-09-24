#User function Template for python3

class Solution:
    def roundToNearest (self, N) : 
        #Complete the function
        M = int(N)
        n = M//10
        k = n*10
        l = (n+1)*10
        a = abs(M-k)
        b = abs(M-l)
        if a == b:
            return k
        elif a>b:
            return l
        else:
            return k



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    s = input()
    ob = Solution()
    res = ob.roundToNearest(s)
    print(res)


# } Driver Code Ends