#User function Template for python3

class Solution:
	def sum_of_ap(self, n, a, d):
		s = 2*a+(n-1)*d
	    ap_sum = (s*n)/2
	    ap_sum = int(ap_sum)
		return ap_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, a, d = input().split()
		n = int(n)
		a = int(a)
		d = int(d)
		ob = Solution();
		ans = ob.sum_of_ap(n, a, d)
		print(ans)
# } Driver Code Ends