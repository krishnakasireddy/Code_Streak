class Solution:
    def printMinIndexChar(self, S, patt):
		#Code here
		k = []
		for i in patt:
		    if i in S:
		        k.append(S.index(i))
	    if len(k)!=0:
	        return S[min(k)]
	    else:
	        return "$"


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	S = input().strip()
    	patt = input().strip()
    	obj = Solution()
    	print(obj.printMinIndexChar(S, patt))
# } Driver Code Ends