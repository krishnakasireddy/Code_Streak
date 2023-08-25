#User function Template for python3

class Solution:
    def areElementsContiguous (self,arr, n) : 
        #Complete the function
        k = 0
        count = 0
        for i in range (n-1,-1,-1):
            if arr[i] == "END":
                k = i
                break
        if k == 0:
            l = list(set(arr))
            for i in l:
                if arr.count(i)%2 != 0:
                    count+=1
            return count
        else:
            k+=1
            a = arr[k:]
            if len(a) == 0:
                return 0
            else:
                b = list(set(a))
                for i in b:
                    if a.count(i)%2 != 0:
                        count+=1
            return count
            





#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(str,input().strip().split()))
    ob=Solution()
    res = ob.areElementsContiguous(arr, n)
    print(res)


# } Driver Code Ends