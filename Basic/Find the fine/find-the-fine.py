#User function Template for python3

class Solution:
    def totalFine(self, n, date, car, fine):
        #Code here
        odd_collect,even_collect = 0,0
        for i in range (n):
            if car[i]%2 == 0:
                odd_collect+=fine[i]
            if car[i]%2 != 0:
                even_collect+=fine[i]
        if date%2 == 0:
            return even_collect
        else:
            return odd_collect
    
    





#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        brr = [int(x) for x in input().strip().split()]
        
        print(Solution().totalFine( n, k, arr, brr))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends