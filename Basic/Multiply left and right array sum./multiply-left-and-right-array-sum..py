#User function Template for python3

def multiply (arr, n) : 
    #Complete the function
    k = n//2
    a = sum(arr[:k])
    b = sum(arr[k:])
    return a*b



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = multiply(arr, n)
    print(ans)
# } Driver Code Ends