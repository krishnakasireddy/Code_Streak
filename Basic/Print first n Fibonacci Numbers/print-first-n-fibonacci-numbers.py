#User function Template for python3

class Solution:
    def printFibb(self,n):
        a = 0
        b = 1
        l = [b]
        n = n-1
        while (n):
            c = a+b
            a = b
            b = c
            l.append(c)
            n = n-1
        return l



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends