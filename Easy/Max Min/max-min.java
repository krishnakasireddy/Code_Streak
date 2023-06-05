//{ Driver Code Starts
//Initial Template for Java

//Initial Template for Java


import java.io.*;
import java.util.*;


class Array {
	public static void main (String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int t = sc.nextInt();
        while(t-- > 0)
        {
            int n = sc.nextInt();
            int a[] = new int[n];
            
            for(int i=0;i<n;i++){
                a[i] = sc.nextInt();
            }
            
            Solution ob = new Solution();
            
            System.out.println(ob.findSum(a,n));
        }
        
	}
}
// } Driver Code Ends


//User function Template for Java

class Solution
{ 
    public static int findSum(int A[],int N) 
    {
        int min = A[0];
        int max = A[N-1];
        for (int i=1;i<N;i++){
            if (min>A[i]){
                int temp = min;
                min = A[i];
                A[i] = temp;
            }
            if (max<A[i]){
                int temp1 = max;
                max = A[i];
                A[i] = temp1;
            }
        }
        int out = max+min;
        return out;
    }
}
