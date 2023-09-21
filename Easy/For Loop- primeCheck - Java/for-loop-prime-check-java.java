//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) {

        // taking input using Scanner class
        Scanner sc = new Scanner(System.in);

        // take testcases
        int t = sc.nextInt();
        while (t-- > 0) {
            // taking the number
            int n = sc.nextInt();
            Geeks obj = new Geeks();

            // caling isPrime method
            // with n as argument
            obj.isPrime(n);
        }
    }
}

// Position this line where user code will be pasted.

// } Driver Code Ends


// User function Template for Java

class Geeks {
    static void isPrime(int n) {
        int fact = 0;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n%i == 0){
                fact = 1;
                break;
            }
        }
        if (fact == 0 && n!=1){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}