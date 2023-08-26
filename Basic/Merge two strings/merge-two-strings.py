#User function Template for python3
class Solution:
    def merge(self, S1, S2):
        s = ''
        a = len(S1)
        b = len(S2)
        k = min(a,b)
        for i in range (k):
            s+=S1[i]+S2[i]
        if a>b:
            s+=S1[b:]
        else:
            s+=S2[a:]
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S1,S2 = map(str,input().strip().split())
        ob = Solution()
        print(ob.merge(S1, S2))
# } Driver Code Ends