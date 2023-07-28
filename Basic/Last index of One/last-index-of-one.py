#User function Template for python3

class Solution:
    def lastIndex(self, s):
        count = 0
        n = len(s)-1
        for i in range (n,-1,-1):
            if s[i]=='1':
                return i
                break
            else:
                count+=1
        if count == len(s):
            return -1
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	s = input()
    	ob = Solution()
    	print(ob.lastIndex(s))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends