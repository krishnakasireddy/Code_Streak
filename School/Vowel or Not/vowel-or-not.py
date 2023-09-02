#User function Template for python3
class Solution:
    def isVowel (ob,c):
        c = c.lower()
        if c == 'a':
            return "YES"
        elif c == 'e':
            return "YES"
        elif c == 'i':
            return "YES"
        elif c == 'o':
            return "YES"
        elif c == 'u':
            return "YES"
        else:
            return "NO"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        c=input()

        ob = Solution()
        print(ob.isVowel(c))
# } Driver Code Ends