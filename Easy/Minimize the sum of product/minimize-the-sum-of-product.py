#User function Template for python3

class Solution:
    def minValue(self, a, b, n):
        a.sort()
        b.sort()
        a = a[::-1]
        min_prod = 0
        for i in range(n):
            min_prod+=a[i]*b[i]
        return min_prod
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.minValue(a, b, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends