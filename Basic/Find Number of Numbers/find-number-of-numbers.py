# Your task is to complete this function
# Function should return an integer
def num(arr, n, k):
    digit_count = 0
    for i in arr:
        while (i):
            num = i%10
            if num == k:
                digit_count+=1
            i = i//10
    return digit_count


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        print(num(arr, n, k))
# Contributed By: Harshit Sidhwa

# } Driver Code Ends