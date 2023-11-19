#User function Template for python3

def isValid(s):
    #code here
    l = s.split('.')
    if len(l)!=4:
        return False
    for i in l:
        if len(i)==0 or len(i)>3:
            return False
        if len(i)>1:
            if i[0]=='0':
                return False
        for j in i:
            if j>='a' and j<='z':
                return False
        x = int(i)
        if x<0 or x>255:
            return False
    return True






#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends