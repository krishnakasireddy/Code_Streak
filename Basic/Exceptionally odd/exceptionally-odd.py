#User function Template for python3

class Solution:
    def getOddOccurrence(self, arr, n):
        # code here 
        d = {}
        for i in arr:
            d[i] = d.get(i,0)+1
        for i,j in d.items():
            if j%2!=0:
                return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getOddOccurrence(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends