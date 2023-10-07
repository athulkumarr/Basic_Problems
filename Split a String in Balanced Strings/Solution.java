class Solution {
    public static int balancedStringSplit(String s) {
        int lCount = 0, rCount = 0, count = 0;
        for( int i = 0; i<s.length(); i++) {
            char ch = s.charAt(i);
            if(ch == 'L')
                lCount++;
            else if(ch == 'R')
                rCount++;
            if(lCount == rCount && lCount != 0) {
                count++;
                lCount = 0;
                rCount = 0;
            }
        }   
        return count;
    }
    
    public static void main(String args[]) {
        System.out.println(balancedStringSplit("RRLLRRLRRLLL"));
    }
}
