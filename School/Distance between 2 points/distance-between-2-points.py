#User function Template for python3
import math
class Solution:
	def distance(self, x1, y1, x2, y2):
		a = abs(x1-x2)
        b = abs(y1-y2)
        k = a**2 + b**2
        m = math.sqrt(k)
        m = round(m)
        return m
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x1, y1, x2, y2 = input().split()
		x1 = int(x1);
		y1 = int(y1);
		x2 = int(x2);
		y2 = int(y2);
		ob = Solution();
		ans = ob.distance(x1, y1, x2, y2)
		print(ans)
# } Driver Code Ends