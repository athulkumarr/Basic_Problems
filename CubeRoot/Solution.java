import java.io.*;
public class Solution {
    // We are using a binary search approach here.
    // We continue our search till the absolute value of (n – mid*mid*mid) < e, 
    //        where e is the required precision
    public static void main(String args[])
    {
        int n = 10;
        double start = 0, end = n, mid, e = 0.000001;
        while(start<=end) {
            mid = (start + end)/2.0;
            if(Math.abs(mid*mid*mid - n) < e)
            {
                System.out.println("Cube Root is " + mid);
                return;
            }
            else if(mid*mid*mid < n) {
                start = mid;
            }
            else {
                end = mid;
            }
        }
    }
}
