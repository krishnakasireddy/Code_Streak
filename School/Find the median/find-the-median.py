#User function Template for python3

class Solution:
	def find_median(self, v):
		v.sort()
		k = len(v)
		m = k//2
		if k%2 == 0:
		    med = (v[m-1]+v[m])//2
		else:
		    med = v[m]
		return med


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends