#User function Template for python3

def game_with_number (arr,  n) : 
    l = []
    for i in range (n-1):
        k = arr[i]|arr[i+1]
        l.append(k)
    l.append(arr[n-1])
    return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)




# } Driver Code Ends